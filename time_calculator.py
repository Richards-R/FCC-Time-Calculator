def add_time(start, duration, day=""):
    
    addingDays = 0
    dayNum = 0
    newDay = ""
    dayCount = ""

    day = day.lower()

    if day != "":   
        weekdayDict = {1 : 'monday',
                       2 : 'tuesday',
                       3 : 'wednesday',
                       4 : 'thursday',
                       5 : 'friday',
                       6 : 'saturday',
                       7 : 'sunday'
                       }
        dayNum = [k for k, v in weekdayDict.items() if v == day][0]           

    #make start time able to be added to with duration. 
    #Update day of the week if needed. Insert added info strings where needed.
    
    # break up time
    splitStartTime = start.split(":")
    hourInt = splitStartTime[0]
    minsInt = splitStartTime[1][:2]
    am_orPm = splitStartTime[1][3:]  

    if am_orPm == "PM":
        hourInt = int(hourInt) + 12
    
    #print(hourInt)
    #print(minsInt)
    #print(am_orPm)

    #break up duration
    dur_splitTime = duration.split(":")
    dur_hourInt = dur_splitTime[0]
    dur_minsInt = dur_splitTime[1][:2]
    
    #print(dur_hourInt)
    #print(dur_minsInt)

    newTimeHour = int(hourInt) + int(dur_hourInt) 
    newTimeMins = int(minsInt) + int(dur_minsInt)
    
    if newTimeMins > 59:
        newTimeHour = newTimeHour + 1
        newTimeMins = newTimeMins - 60 
       
    if newTimeHour > 24:
        addingDays = addingDays + (newTimeHour//24)
        #print(addingDays)
        newTimeHour = newTimeHour % 24
        #print("remainder: ", newTimeMins)
        #newTimeHour = newTimeHour + addingDays
        
    if newTimeHour > 12:
        newTimeHour = newTimeHour - 12
        am_orPm = "PM"
    else: 
        am_orPm = "AM"

    #print(dayNum)
    #print("addingDays :", addingDays)
    
    newDayNum = dayNum + addingDays

    if addingDays == 1:
        dayCount = " (next day)"
        
    if addingDays > 1:
        dayCount = " (" + str(addingDays) + " days later)"

    if newDayNum > 7:
        newDayNum = newDayNum % 7
    #print(newDayNum)

    if day != "": 
        newDay = [v for k, v in weekdayDict.items() if k == newDayNum][0]
        newDay = newDay.capitalize()
    
    if newTimeMins < 10:
        zerofiller = "0"
    else: 
        zerofiller = ""

    if newTimeHour == 12 and am_orPm == "AM":
        am_orPm = "PM"

    if newTimeHour == 0 and am_orPm == "AM":
        newTimeHour = 12

    new_time = str(newTimeHour) + ":" + zerofiller + str(newTimeMins) + " " + am_orPm
    
    #print("Input params:", start, duration, day)
    if day == "":
        new_time = new_time + dayCount
    else:
        new_time = new_time + ", "  + newDay + dayCount 
    #print(new_time)    
    return new_time