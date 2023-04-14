def concatenate_args(*word):
    result = ""
    for nam in word:
        result += nam
    return result
   

def concatenate_kwargs(**kwargs):
    answer = ""
    for arg in kwargs.values():
        answer += arg
    return answer 
