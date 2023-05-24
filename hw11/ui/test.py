# from datetime import datetime, timedelta
#
#
# class Record:
#
#     def __init__(self, d=None):
#         self.d = d
#
#     def days_to_birthday(self):
#         now = datetime.now()
#         ts_now = now.timestamp()
#         one_year_interval = timedelta(weeks=52)
#         birthday = datetime.strptime(self.d.birthday, '%d-%m-%Y').date()
#         ts_bd_0 = datetime(year=now.year, month=birthday.month, day=birthday.day).timestamp()
#         delta = (ts_bd_0 - ts_now) // (24 * 3600) + 1
#         if delta > 0:
#             print(int(delta))
#         elif delta < 0:
#             print(int(delta + one_year_interval.days + 1))
#         else:
#             print('Say Happy Birthday to contact today!')
#
#
# class Birthday:
#
#     def __init__(self, birthday):
#         self.birthday = birthday
#
#     def __str__(self):
#         return self.birthday
#
#
# record = Record(Birthday('23-05-1980'))
# record.days_to_birthday()
