# from django import template

# register = template.Library()

# @register.filter
# def calculate_total_marks(result):
#     return result.subject_assignment_marks + result.subject_exam_marks

from django import template

register = template.Library()

@register.simple_tag
def calculate_total_marks(subject_exam_marks, subject_assignment_marks):
    return subject_exam_marks + subject_assignment_marks