class Summary_Process:
    def __init__(self, summary_send):
        self.summary_send = summary_send

    def run_process (self):
        self.summary_send.submitReport()

