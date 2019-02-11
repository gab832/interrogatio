import abc
import six


from collections import namedtuple

from ...enums import Mode

class Rule:
    def __init__(self, fg='', bg='', attr=''):
        self.fg = fg
        self.bg = bg
        self.attr = attr

class ComponentStyle(six.with_metaclass(abc.ABCMeta, object)):

    def __init__(self, mode, **kwargs):
        assert mode in [Mode.PROMPT,  Mode.DIALOG]
        self._mode = mode
        for arg in kwargs.values():
            assert isinstance(arg, Rule)

    @abc.abstractmethod
    def to_style(self):
        pass

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __hash__(self):
        return hash('{}.{}'.format(self._mode, self.__class__))

class ErrorStyle(ComponentStyle):
    def __init__(self, mode, message=Rule(fg='darkred', 
                                          attr='bold underline')):
        super(ErrorStyle, self).__init__(mode, message=message)
        self._message = message

    def to_style(self):
        rules = []
        
        rules.append(
            (
                '{}.error'.format(self._mode), 
                'bg:{} {} {}'.format(
                    self._message.bg or 'default',
                    self._message.fg or '',
                    self._message.attr or ''
                ).strip()
            )
        )

        return rules    

class InputStyle(ComponentStyle):

    def __init__(self,
        mode,
        question=Rule(fg='darkblue'),
        answer=Rule(fg='orange', attr='bold')):

        super(InputStyle, self).__init__(mode, 
                                         question=question,
                                         answer=answer)

        self._question = question
        self._answer = answer

    def to_style(self):
        rules = []
        
        rules.append(
            (
                '{}.input.question'.format(self._mode), 
                'bg:{} {} {}'.format(
                    self._question.bg or 'default',
                    self._question.fg or '',
                    self._question.attr or ''
                ).strip()
            )
        )

        rules.append(
            (
                '{}.input.answer'.format(self._mode), 
                'bg:{} {} {}'.format(
                    self._answer.bg or 'default',
                    self._answer.fg or '',
                    self._answer.attr or ''
                ).strip()
            )
        )          
        return rules


class PasswordStyle(ComponentStyle):
    def __init__(self,
        mode,
        question=Rule(fg='darkblue'),
        answer=Rule(fg='orange', attr='bold')):

        super(PasswordStyle, self).__init__(mode, 
                                         question=question,
                                         answer=answer)

        self._question = question
        self._answer = answer

    def to_style(self):
        rules = []
        
        rules.append(
            (
                '{}.password.question'.format(self._mode), 
                'bg:{} {} {}'.format(
                    self._question.bg or 'default',
                    self._question.fg or '',
                    self._question.attr or ''
                ).strip()
            )
        )

        rules.append(
            (
                '{}.password.answer'.format(self._mode), 
                'bg:{} {} {}'.format(
                    self._answer.bg or 'default',
                    self._answer.fg or '',
                    self._answer.attr or ''
                ).strip()
            )
        )
        return rules


class SelectOneStyle(ComponentStyle):

    def __init__(self,
        mode,
        question=Rule(fg='darkblue'),
        answer=Rule(fg='darkblue', attr='bold'),
        selected=Rule(fg='cyan'),
        checked=Rule(fg='orange', attr='bold')):

        super(SelectOneStyle, self).__init__(
            mode,
            question=question,
            answer=answer,
            selected=selected,
            checked=checked
        )
        self._question = question
        self._answer = answer
        self._selected = selected
        self._checked = checked


    def to_style(self):
        rules = []

        rules.append(
            (
                '{}.selectone.question'.format(self._mode), 
                'bg:{} {} {}'.format(
                    self._question.bg or 'default',
                    self._question.fg or '',
                    self._question.attr or ''
                ).strip()
            )
        )

        rules.append(
            (
                '{}.selectone.answer'.format(self._mode), 
                'bg:{} {} {}'.format(
                    self._answer.bg or 'default',
                    self._answer.fg or '',
                    self._answer.attr or ''
                ).strip()
            )
        )

        rules.append(
            (
                '{}.selectone.answer radio'.format(self._mode), 
                'bg:{} {} {}'.format(
                    self._answer.bg or 'default',
                    self._answer.fg or '',
                    self._answer.attr or ''
                ).strip()
            )
        )

        rules.append(
            (
                '{}.selectone.answer radio-selected'.format(self._mode), 
                'bg:{} {} {}'.format(
                    self._selected.bg or 'default',
                    self._selected.fg or '',
                    self._selected.attr or ''
                ).strip()
            )
        )

        rules.append(
            (
                '{}.selectone.answer radio-checked'.format(self._mode), 
                'bg:{} {} {}'.format(
                    self._checked.bg or 'default',
                    self._checked.fg or '',
                    self._checked.attr or ''
                ).strip()
            )
        )
        return rules


class SelectManyStyle(ComponentStyle):

    def __init__(self,
        mode,
        question=Rule(fg='darkblue'),
        answer=Rule(fg='darkblue', attr='bold'),
        selected=Rule(fg='cyan'),
        checked=Rule(fg='orange', attr='bold')):

        super(SelectManyStyle, self).__init__(
            mode,
            question=question,
            answer=answer,
            selected=selected,
            checked=checked
        )
        self._question = question
        self._answer = answer
        self._selected = selected
        self._checked = checked


    def to_style(self):
        rules = []

        rules.append(
            (
                '{}.selectmany.question'.format(self._mode), 
                'bg:{} {} {}'.format(
                    self._question.bg or 'default',
                    self._question.fg or '',
                    self._question.attr or ''
                ).strip()
            )
        )

        rules.append(
            (
                '{}.selectmany.answer'.format(self._mode), 
                'bg:{} {} {}'.format(
                    self._answer.bg or 'default',
                    self._answer.fg or '',
                    self._answer.attr or ''
                ).strip()
            )
        )

        rules.append(
            (
                '{}.selectmany.answer checkbox'.format(self._mode), 
                'bg:{} {} {}'.format(
                    self._answer.bg or 'default',
                    self._answer.fg or '',
                    self._answer.attr or ''
                ).strip()
            )
        )

        rules.append(
            (
                '{}.selectmany.answer checkbox-selected'.format(self._mode), 
                'bg:{} {} {}'.format(
                    self._selected.bg or 'default',
                    self._selected.fg or '',
                    self._selected.attr or ''
                ).strip()
            )
        )

        rules.append(
            (
                '{}.selectmany.answer checkbox-checked'.format(self._mode), 
                'bg:{} {} {}'.format(
                    self._checked.bg or 'default',
                    self._checked.fg or '',
                    self._checked.attr or ''
                ).strip()
            )
        )
        return rules