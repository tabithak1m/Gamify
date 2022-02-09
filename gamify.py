def get_cur_hedons():
    '''
    This function returns the number of hedons that the user has accumulated so far.
    '''
    #hedons are "fun points" the user accumulates when preforming exercise activities
    global hedons
    return hedons

def get_cur_health():
    '''
    This function returns the number of health points that the user has accumulated so far
    '''
    #health_points are health points the user accumulates when preforming exercise activities
    global health_points
    return health_points


def offer_star(activity):
    '''
    This function simulates a offering the user a star for engaging in the exercise activity.
    '''
    #star keeps track of how many stars have been offered
    #time keeps track of the time interval within the simulation
    #star_time a list that keeps track of when the last star was offered
    #x == 0 boolean disables function
    global star, time, exc_time, star_time, x

    #when more than three stars were offered within the span of two hours - no more hedons ever

    if x == 0:
        if activity == "running" or "textbooks":
            if len(act_duration) - 1 >= 6:
                #if star was offered more than three times
                if act_duration[-1] - act_duration[-5] > 120:
                    #if the three stars were offered not within 2 hours
                    star.append(activity)
                    star_time.append(time) #remember what time was when the star was offered
                else:
                    #if the three stars were offered within 2 hours
                    #lost interest - wont get additional hedons dur to stars ever
                    x == 1 #disables function
            else:
                #if star was offered less than three times
                star.append(activity)
                star_time.append(time) #remember what time was when the star was offered



def perform_activity(activity, duration):
    '''
    This function simulates the user's performing activity for duration mintues.
    '''
    global hedons
    global health_points
    global exc_time
    global time
    global prev_act #the list that contains activities that were done
    global star_time
    global star #list of activities where star was offered
    global act_duration #list that stores the activity and duration for when star was taken
    global rest_time #the time user rests for (resets everytime they do a diff activity)


    if star[-1] == activity and star_time[-1] == time:
        #when user is offered star:
        act_duration.append(activity)
        act_duration.append(time) #remember what time was when the activity was done
        if duration <= 10:
            hedons += 3 * duration
        else:
            hedons = 3 * 10

    prev_act.append(activity)
    time += duration #the total time (time at that moment)

    if activity == "running" or "textbooks":
        exc_time.append(duration) #keep track of time spent on excercising


    if activity == "resting":
        rest_time += duration #keep track of time spend on resting


    if activity == "running":
        if prev_act[-2] == "resting" and rest_time >= 120:
            #when user isn't tired
            if duration <= 180:
                health_points += 3 * duration
                if duration <= 10:
                    hedons += 2 * duration
                    rest_time = 0
                else:
                    hedons += 2 * 10 + -2 * (duration - 10)
                    rest_time = 0
            elif duration > 180:
                health_points += 3 * 180 + 1 * (duration - 180)
                hedons += 2 * 10 + -2 * (duration - 10)
                rest_time = 0
        else:
            #when user is tired
            hedons += -2 * duration
            if duration <= 180:
                health_points += 3 * duration
                rest_time = 0
            elif duration > 180:
                health_points += 3 * 180 + 1 * (duration - 180)
                rest_time = 0

    elif activity == "textbooks":
        if prev_act[-2] == "resting" and rest_time >= 120:
            #when user isn't tired
            if duration <= 20:
                hedons += 1 * duration
                health_points += 2 * duration
                rest_time = 0
            else:
                hedons += 1 * 20 + -1 * (duration - 20)
                health_points += 2 * duration
                rest_time = 0
        else:
            #when user isn't on star and is tired
            hedons += -2 * duration
            health_points += 2 * duration
            rest_time = 0



def star_can_be_taken(activity):
    '''
    This function returns True iff a star can be used to get more hedons for activity activity.
    '''
    global hedons, star, time, exc_time, prev_act, act_duration

    if prev_act[-1] == activity:
        if len(act_duration) >= 6:
            #when more than 3 stars were offered
            if act_duration[-1] - act_duration[-5] <= 120:
                #when 3 stars were offered within 2 hrs
                return False
            else:
                return True
        else:
            return True


def most_fun_activity_minute():
    '''
    This function returns the activity (one of "resting", "running", or "textbooks") which would give the most hedons if the person performed it for one minute at the current time
    '''
    global star, prev_act, star_time, rest_time


    if prev_act[-1] == "resting" and rest_time >= 120:
        #if user isn't tired
        return "running"
    else:
        #if user is tired
        if star[-1] == "running" and star_time[-1] == time:
            #if star is taken but tired
            return "running"
        else:
            #if star isn't taken and tired:
            return "resting"

def initialize():
    '''
    This function initializes all the global variables in the program
    '''
    global hedons, health_points, exc_time, time, prev_act, star_time, act_duration, star, x, rest_time

    hedons = 0
    health_points = 0
    exc_time = [0]
    time = 0
    prev_act = ["resting"]
    star_time = [0]
    act_duration = [0]
    star = [0]
    x = 0
    rest_time = 120


if __name__ == "__main__":
    initialize()
    perform_activity("running", 30)
    print(get_cur_hedons())
    print(get_cur_health())
    print(most_fun_activity_minute())
    perform_activity("resting", 30)
    offer_star("running")
    print(most_fun_activity_minute())
    perform_activity("textbooks", 30)
    print(get_cur_health())



































