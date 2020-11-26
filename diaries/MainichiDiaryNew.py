from diaries.AbstractDiary import AbstractDiary


class MainichiDiaryNew(AbstractDiary):

    def get_date(self):
        return "2020-11-26"

    def get_summary(self):
        return "今日は走って"

    def get_author(self):
        return "Sample"