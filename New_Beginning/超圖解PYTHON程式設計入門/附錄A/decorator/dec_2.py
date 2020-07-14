def convert_date(log):
    return '/'.join([d for d in log.split('-')])

def wrapper(func):
    def inner(logs):
        return [func(d) for d in logs]
    return inner

convert_date = wrapper(convert_date)

dates = [
    '2018-12-25',
    '2019-03-13',
    '2019-08-24'
]

print(convert_date(dates))