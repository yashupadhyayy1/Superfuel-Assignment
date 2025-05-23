###############################################################################
#
#  Welcome to Baml! To use this generated code, please run the following:
#
#  $ pip install baml-py
#
###############################################################################

# This file was generated by BAML: please do not edit it. Instead, edit the
# BAML files and re-generate this code.
#
# ruff: noqa: E501,F401
# flake8: noqa: E501,F401
# pylint: disable=unused-import,line-too-long
# fmt: off
import typing
from baml_py.baml_py import FieldType, EnumValueBuilder, EnumBuilder, ClassBuilder
from baml_py.type_builder import TypeBuilder as _TypeBuilder, ClassPropertyBuilder, ClassPropertyViewer, EnumValueViewer
from .globals import DO_NOT_USE_DIRECTLY_UNLESS_YOU_KNOW_WHAT_YOURE_DOING_RUNTIME


class TypeBuilder(_TypeBuilder):
    def __init__(self):
        super().__init__(classes=set(
          ["Experience","MathTool","Plan","Resume","ToolCall",]
        ), enums=set(
          []
        ), runtime=DO_NOT_USE_DIRECTLY_UNLESS_YOU_KNOW_WHAT_YOURE_DOING_RUNTIME)


    @property
    def Experience(self) -> "ExperienceAst":
        return ExperienceAst(self)

    @property
    def MathTool(self) -> "MathToolAst":
        return MathToolAst(self)

    @property
    def Plan(self) -> "PlanAst":
        return PlanAst(self)

    @property
    def Resume(self) -> "ResumeAst":
        return ResumeAst(self)

    @property
    def ToolCall(self) -> "ToolCallAst":
        return ToolCallAst(self)





class ExperienceAst:
    def __init__(self, tb: _TypeBuilder):
        _tb = tb._tb # type: ignore (we know how to use this private attribute)
        self._bldr = _tb.class_("Experience")
        self._properties: typing.Set[str] = set([ "company",  "role",  "duration",  "location", ])
        self._props = ExperienceProperties(self._bldr, self._properties)

    def type(self) -> FieldType:
        return self._bldr.field()

    @property
    def props(self) -> "ExperienceProperties":
        return self._props


class ExperienceViewer(ExperienceAst):
    def __init__(self, tb: _TypeBuilder):
        super().__init__(tb)

    
    def list_properties(self) -> typing.List[typing.Tuple[str, ClassPropertyViewer]]:
        return [(name, ClassPropertyViewer(self._bldr.property(name))) for name in self._properties]



class ExperienceProperties:
    def __init__(self, bldr: ClassBuilder, properties: typing.Set[str]):
        self.__bldr = bldr
        self.__properties = properties

    

    @property
    def company(self) -> ClassPropertyViewer:
        return ClassPropertyViewer(self.__bldr.property("company"))

    @property
    def role(self) -> ClassPropertyViewer:
        return ClassPropertyViewer(self.__bldr.property("role"))

    @property
    def duration(self) -> ClassPropertyViewer:
        return ClassPropertyViewer(self.__bldr.property("duration"))

    @property
    def location(self) -> ClassPropertyViewer:
        return ClassPropertyViewer(self.__bldr.property("location"))

    

class MathToolAst:
    def __init__(self, tb: _TypeBuilder):
        _tb = tb._tb # type: ignore (we know how to use this private attribute)
        self._bldr = _tb.class_("MathTool")
        self._properties: typing.Set[str] = set([ "name",  "description", ])
        self._props = MathToolProperties(self._bldr, self._properties)

    def type(self) -> FieldType:
        return self._bldr.field()

    @property
    def props(self) -> "MathToolProperties":
        return self._props


class MathToolViewer(MathToolAst):
    def __init__(self, tb: _TypeBuilder):
        super().__init__(tb)

    
    def list_properties(self) -> typing.List[typing.Tuple[str, ClassPropertyViewer]]:
        return [(name, ClassPropertyViewer(self._bldr.property(name))) for name in self._properties]



class MathToolProperties:
    def __init__(self, bldr: ClassBuilder, properties: typing.Set[str]):
        self.__bldr = bldr
        self.__properties = properties

    

    @property
    def name(self) -> ClassPropertyViewer:
        return ClassPropertyViewer(self.__bldr.property("name"))

    @property
    def description(self) -> ClassPropertyViewer:
        return ClassPropertyViewer(self.__bldr.property("description"))

    

class PlanAst:
    def __init__(self, tb: _TypeBuilder):
        _tb = tb._tb # type: ignore (we know how to use this private attribute)
        self._bldr = _tb.class_("Plan")
        self._properties: typing.Set[str] = set([ "calls",  "explanation", ])
        self._props = PlanProperties(self._bldr, self._properties)

    def type(self) -> FieldType:
        return self._bldr.field()

    @property
    def props(self) -> "PlanProperties":
        return self._props


class PlanViewer(PlanAst):
    def __init__(self, tb: _TypeBuilder):
        super().__init__(tb)

    
    def list_properties(self) -> typing.List[typing.Tuple[str, ClassPropertyViewer]]:
        return [(name, ClassPropertyViewer(self._bldr.property(name))) for name in self._properties]



class PlanProperties:
    def __init__(self, bldr: ClassBuilder, properties: typing.Set[str]):
        self.__bldr = bldr
        self.__properties = properties

    

    @property
    def calls(self) -> ClassPropertyViewer:
        return ClassPropertyViewer(self.__bldr.property("calls"))

    @property
    def explanation(self) -> ClassPropertyViewer:
        return ClassPropertyViewer(self.__bldr.property("explanation"))

    

class ResumeAst:
    def __init__(self, tb: _TypeBuilder):
        _tb = tb._tb # type: ignore (we know how to use this private attribute)
        self._bldr = _tb.class_("Resume")
        self._properties: typing.Set[str] = set([ "name",  "email",  "experience",  "skills", ])
        self._props = ResumeProperties(self._bldr, self._properties)

    def type(self) -> FieldType:
        return self._bldr.field()

    @property
    def props(self) -> "ResumeProperties":
        return self._props


class ResumeViewer(ResumeAst):
    def __init__(self, tb: _TypeBuilder):
        super().__init__(tb)

    
    def list_properties(self) -> typing.List[typing.Tuple[str, ClassPropertyViewer]]:
        return [(name, ClassPropertyViewer(self._bldr.property(name))) for name in self._properties]



class ResumeProperties:
    def __init__(self, bldr: ClassBuilder, properties: typing.Set[str]):
        self.__bldr = bldr
        self.__properties = properties

    

    @property
    def name(self) -> ClassPropertyViewer:
        return ClassPropertyViewer(self.__bldr.property("name"))

    @property
    def email(self) -> ClassPropertyViewer:
        return ClassPropertyViewer(self.__bldr.property("email"))

    @property
    def experience(self) -> ClassPropertyViewer:
        return ClassPropertyViewer(self.__bldr.property("experience"))

    @property
    def skills(self) -> ClassPropertyViewer:
        return ClassPropertyViewer(self.__bldr.property("skills"))

    

class ToolCallAst:
    def __init__(self, tb: _TypeBuilder):
        _tb = tb._tb # type: ignore (we know how to use this private attribute)
        self._bldr = _tb.class_("ToolCall")
        self._properties: typing.Set[str] = set([ "tool",  "args",  "description", ])
        self._props = ToolCallProperties(self._bldr, self._properties)

    def type(self) -> FieldType:
        return self._bldr.field()

    @property
    def props(self) -> "ToolCallProperties":
        return self._props


class ToolCallViewer(ToolCallAst):
    def __init__(self, tb: _TypeBuilder):
        super().__init__(tb)

    
    def list_properties(self) -> typing.List[typing.Tuple[str, ClassPropertyViewer]]:
        return [(name, ClassPropertyViewer(self._bldr.property(name))) for name in self._properties]



class ToolCallProperties:
    def __init__(self, bldr: ClassBuilder, properties: typing.Set[str]):
        self.__bldr = bldr
        self.__properties = properties

    

    @property
    def tool(self) -> ClassPropertyViewer:
        return ClassPropertyViewer(self.__bldr.property("tool"))

    @property
    def args(self) -> ClassPropertyViewer:
        return ClassPropertyViewer(self.__bldr.property("args"))

    @property
    def description(self) -> ClassPropertyViewer:
        return ClassPropertyViewer(self.__bldr.property("description"))

    




__all__ = ["TypeBuilder"]