import random

# define and initialize the parameters of the Poisson distributions
lambd_in = 0.5
lambd_out = 0.4

# bank variables
closing_time = 100  # initialize the bank closing time
overtime = 0  # overtime the employees need to be paid for

# queue variables
num_arrivals = 0  # number of people in the que
num_departures = 0  # number of people who have been served
n = 0  # length of the queue
max_line_length = 0  # the maximum length of the waiting line:

# time variables
t = 0  # set the time of first arrival to 0
time_depart = float('inf')  # set the first time of departure to infinity
time_arrive = random.expovariate(lambd_in)  # generate the first arrival

departures = []
arrivals = []

while t < closing_time or n >= 0:

    # case 1 - within business hours, a customer arrives before any customer leaves the queue
    if time_arrive <= time_depart and time_arrive <= closing_time:

        t = time_arrive  # move time along to the time of the new arrival
        num_arrivals += 1  # increase the number of customers with the additional arrival
        n += 1  # we have an additional customer, increase the size of the waiting line by 1

        # generate time of next arrival
        time_arrive = random.expovariate(lambd_in) + t

        # append the new customer to the arrival list
        arrivals.append(t)
        print("Arrival ", num_arrivals, "at time ", t)

        # generate time of departure
        if n == 1:
            Y = random.expovariate(lambd_out)
            time_depart = t + Y

        ''' 
        print('Arrivals', arrivals)
        print('Departures', departures)
        '''

        # case 2 - within business hours, a customer departs before the next arrival
    elif time_depart < time_arrive and time_depart <= closing_time:

        # advance time to the next departure time
        t = time_depart

        # one more person served -> increase the count of clients who have been served
        num_departures += 1

        # update the departure list
        departures.append(t)
        print("Departure ", num_departures, "at time ", t)

        # one less person in line -> decrease the size of the waiting line
        n -= 1

        # if the queue is empt -> set the time of the next departure to infinity
        if n == 0:
            time_depart = float('inf')

        # if the queue isn't empty, generate the next time of departure
        else:
            Y = random.expovariate(lambd_out)
            time_depart = t + Y

        ''' 
        print('Arrivals', arrivals)
        print('Departures', departures)    
        '''

        # case 3 - next arrival/departure happens after closing time and there are people still in the queue
    elif min(time_arrive, time_depart) > closing_time and n > 0:

        # advance time to next departure
        t = time_depart

        # update the departure list
        departures.append(t)

        # update the number of departures/clients served
        num_departures += 1  # one more person served

        print("Departure ", num_departures, "at time ", t)

        # update the queue
        n -= 1  # one less person in the waiting line

        # if line isn't empty, generate the time of the next departure
        if n > 0:
            Y = random.expovariate(lambd_out)
            time_depart = t + Y

        ''' 
        print('Arrivals', arrivals)
        print('Departures', departures) 
        '''

        # case 4 - next arrival/departure happens after closing time and there is nobody left in the queue
    elif min(time_arrive, time_depart) > closing_time and n == 0:

        # calculate overtime
        overtime = max(t - closing_time, 0)
        print('Overtime = ', overtime)

        '''
        print('Arrivals', arrivals)
        print('Departures', departures)
        '''

        break