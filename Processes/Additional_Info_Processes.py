from Model.Additional_Information_Page_Model import AdditionalInformationDetailsModel
class AdditionalInfoProcess:
    def __init__(self, additional_info):
        self.additional_info = additional_info

    def run_processes(self, data:AdditionalInformationDetailsModel):
        self.additional_info.select_Option(data)




