'''
Your company built an in-house calendar tool called HiCal. You want to add a feature to see the times in a day when everyone is available.
'''

def condense_meeting_time(meeting_range):
    new_meeting_range = []
    l = len(meeting_range)
    i=0
    while i < l:
        flag = 0
        j = i+1
        while j < l:
            if meeting_range[i][1]>meeting_range[j][0]:
                start_time = min(meeting_range[i][0],meeting_range[j][0])
                end_time = max(meeting_range[i][1],meeting_range[j][1])
                if (start_time, end_time) not in new_meeting_range:
                    new_meeting_range.append((start_time, end_time))
                del(meeting_range[j])
                flag = 1
                l = len(meeting_range)
            else:
                j += 1
        if not flag:
            new_meeting_range.append(meeting_range[i])
        i += 1
    return new_meeting_range

def merge_ranges(meetings):
    # sort by start times
    sorted_meetings = sorted(meetings)
    # initialize merged_meetings with the earliest meeting
    merged_meetings = [sorted_meetings[0]]

    for current_meeting_start, current_meeting_end in sorted_meetings[1:]:
        last_merged_meeting_start, last_merged_meeting_end = merged_meetings[-1]
        # if the current and last meetings overlap, use the latest end time
        if (current_meeting_start <= last_merged_meeting_end):
            merged_meetings[-1] = (last_merged_meeting_start, max(last_merged_meeting_end, current_meeting_end))

        # add the current meeting since it doesn't overlap
        else:
            merged_meetings.append((current_meeting_start, current_meeting_end))

    return merged_meetings
meetings = [(3, 7), (5, 10), (2, 6), (11, 14)]
print merge_ranges(meetings)