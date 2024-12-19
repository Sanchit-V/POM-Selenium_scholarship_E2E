class Additional_Info_Process:
    def __init__(self, additional_info):
        self.additional_info = additional_info

    def run_processes(self, additional_type, Text_Additional_field, selected_language):
        self.additional_info.select_Option(additional_type, Text_Additional_field, selected_language)




