"""Given an array of meeting time intervals consisting of start and
end times[[s1,e1],[s2,e2],...](si< ei), determine if a person could
attend all meetings."""

def can_attend_meeting(arr):

    
    for i in range(1,len(arr)):

        current=arr[i][0]         
        previous=arr[i-1][1]

        if current<previous:    # checking previous end and next starting if it is inside the range it will make the meeting overlap and return false
            return False
        
    return True

arr=[[0,2],[5,10],[15,20]]
print(can_attend_meeting(arr))