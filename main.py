from diaries.DiarySample import DiarySample
from diaries.MainichiDiaryNew import MainichiDiaryNew

diaries = [DiarySample(),
MainichiDiaryNew(),
 ]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()