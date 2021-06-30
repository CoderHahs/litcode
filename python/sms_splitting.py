# SMS splitting
# Instructions
# Given an input string of arbitrary length, output SMS-compliant
# segments with suffixes.
# • A SMS-compliant segment is of length 160 characters or less.
# • Do not generate segments if the input fits in a single message.
# • A segment suffix looks like "(1/5)" for the firstoffive segments.
# • The segment content and suffix must both fit in the segment.
# You must complete the function/method stub to return an
# array of message segments.
# v Input Constraints
# • Inputs will only consist of A-Z. a-Z. spaces commas and periods
# • Your implementation can expecta maximum of 9 segments per input.
# v Extra Credit Case
# • The third test case has an additional output constraint: do not split
# words between segments! You should be able to iterate on your
# existing implementation.
# • Words will be delimited by a single space. Do not split on any other
# punctuation. You do not need to account for "unbreakable" i.e
# extremely long words in the input.
# Spaces between words should be preserved in the first segment
# unless that violates the SMS length constraint, in which case the
# space should be included in the next segment.
# For example, given the following text:
# Lorem ipsum dolor sit amet, consectetur adipiscing
# elit. Phasellus consequat nec dui quis maximus .
# Praesent vehicula feugiat condimentum. Nunc porta
# vulputate elit sit amet . Vivamus volutpat
# accumsan consequat . Nulla mattis odio erat, vel
# convallis neque semper nec. Integer a pharetra
# The segment break would fall between "porta" and "volputate" with
# the space fitting in the first segrnent. The output would be:

def segments(message):
    # Write your code here
    
    # sms = []
    # l = len(message) // 160 + 1
    # segment = 1
    # for i in range(0, l*160, 160):
    #     print(i, l, l*160)
    #     if ()
    #     sms.append(message[i:i+160] + '(' + str(segment)+'/'+str(l)+')')
    #     segment+= 1
    # return sms

    if (len(message) <= 160):
        return [message[:]]
    
    l = len(message) // 160 + 1
    segment = 1
    message = message.split (" ")
    sms = []
    partition = ''
    flag = False
    for word in message:
        if (len(partition + word) <= 155):
            if (len(partition + word + ' ') > 155):
                partition += word
                flag = True
            else:
                partition += word + ' '
        else:
            partition += "(" + str(segment)+ "/" + str(l) + ")"
            sms.append(partition)
            segment += 1
            if (flag == True):
                partition = " " + word + ' '
                flag = False
            else:
                partition = word + ' '
    partition = partition[:-1] + "(" + str(segment)+ "/" + str(l) + ")"
    if (segment == l):
        sms.append(partition)
    return sms