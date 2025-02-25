# import torch.nn as nn
#
# class TeacherStudent(nn.Module):
#     def __init__(self, teacher, student):
#         super(TeacherStudent, self).__init__()
#         self.teacher = teacher
#         self.student = student
#
#     def _anonymize_text(self, text):
#         return text
#
#     def _de_anonymize_text(self, short_response, original_text):
#         de_anonymized_text = "The original text is: |" + original_text + "| and the teacher told you: |" + short_response + "|"
#         return de_anonymized_text
#
#     def forward(self, original_text):
#         anonymized_text = self._anonymize_text(original_text)
#         short_response = self.teacher(anonymized_text)
#         de_anonymized_text = self._de_anonymize_text(short_response, original_text)
#         full_response = self.student(de_anonymized_text)
#
#         return full_response
#
#
