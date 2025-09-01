from Pydentic_Model.models import AdditionalInfoData
class AdditionalInfoProcess:
    def __init__(self, additional_info):
        self.additional_info = additional_info

    def run_processes(self, data:AdditionalInfoData):
        self.additional_info.select_Option(data)




