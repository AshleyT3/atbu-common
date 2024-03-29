# Copyright 2022 Ashley R. Thomas
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
r"""ATBU common exceptions.
"""

# pylint: disable=missing-class-docstring

from dataclasses import dataclass
import sys
import traceback
from typing import Literal

ANOMALY_KINDS = Literal["exception", "cancelled", "unexpected state"]
ANOMALY_KIND_EXCEPTION = "exception"
ANOMALY_KIND_CANCELLED = "cancelled"
ANOMALY_KIND_UNEXPECTED_STATE = "unexpected state"


@dataclass
class Anomaly:
    kind: ANOMALY_KINDS
    exception: Exception = None
    message: str = None


class AtbuException(Exception):
    def __init__(self, message: str, cause=None):
        super().__init__(message)
        self.message = message
        self._cause = cause

    @property
    def cause(self):
        return self._cause

    def __str__(self):
        if not self._cause:
            return f"{self.message}"
        else:
            return f"{self.message} cause={self._cause}"


class LocationDoesNotExistException(AtbuException):
    def __init__(self, message: str = None, cause=None):
        super().__init__(message=message, cause=cause)


class ConfigFileNotFoundError(AtbuException):
    def __init__(self, message: str = None, cause=None):
        super().__init__(message=message, cause=cause)


class InvalidConfigurationValue(AtbuException):
    def __init__(self, message: str = None, cause=None):
        super().__init__(message=message, cause=cause)


class InvalidConfigurationFile(AtbuException):
    def __init__(self, message: str = None, cause=None):
        super().__init__(message=message, cause=cause)


class InvalidConfiguration(AtbuException):
    def __init__(self, message: str = None, cause=None):
        super().__init__(message=message, cause=cause)


class ConfigSectionNotFound(AtbuException):
    def __init__(self, message: str = None, cause=None):
        super().__init__(message=message, cause=cause)


class ConfigValueNotFound(AtbuException):
    def __init__(self, message: str = None, cause=None):
        super().__init__(message=message, cause=cause)


class ObjectDoesNotExistError(AtbuException):
    def __init__(self, message: str = None, cause=None):
        super().__init__(message=message, cause=cause)


class ContainerAlreadyExistsError(AtbuException):
    def __init__(self, message: str = None, cause=None):
        super().__init__(message=message, cause=cause)


class InvalidContainerNameError(AtbuException):
    def __init__(self, message: str = None, cause=None):
        super().__init__(message=message, cause=cause)


class ContainerAutoCreationFailed(AtbuException):
    def __init__(self, message: str = None, cause=None):
        super().__init__(message=message, cause=cause)


class RetryLimitReached(AtbuException):
    def __init__(self, message: str = None, cause=None):
        self._cause = cause
        super().__init__(message=message, cause=cause)


class FileChangedWhileCalculatingHash(AtbuException):
    def __init__(self, message: str = None, cause=None):
        self._cause = cause
        super().__init__(message=message, cause=cause)


class ExpectedDirectoryIsFileError(AtbuException):
    def __init__(self, message: str = None, cause=None):
        self._cause = cause
        super().__init__(message=message, cause=cause)


class SingletonAlreadyCreated(AtbuException):
    def __init__(self, message: str = None, cause=None):
        self._cause = cause
        super().__init__(message=message, cause=cause)


class QueueListenerAlreadyStarted(AtbuException):
    def __init__(self, message: str = None, cause=None):
        self._cause = cause
        super().__init__(message=message, cause=cause)


class QueueListenerNotStarted(AtbuException):
    def __init__(self, message: str = None, cause=None):
        self._cause = cause
        super().__init__(message=message, cause=cause)


class UnexpectedOperation(AtbuException):
    def __init__(self, message: str = None, cause=None):
        self._cause = cause
        super().__init__(message=message, cause=cause)


class EncryptionAlreadyEnabledError(AtbuException):
    def __init__(self, message: str = None, cause=None):
        self._cause = cause
        super().__init__(message=message, cause=cause)


class InvalidStateError(AtbuException):
    def __init__(self, message: str = None, cause=None):
        self._cause = cause
        super().__init__(message=message, cause=cause)


class UserAbortException(AtbuException):
    def __init__(self, message: str = None, cause=None):
        self._cause = cause
        super().__init__(message=message, cause=cause)


class StateChangeDisallowedError(AtbuException):
    def __init__(self, message: str = None, cause=None):
        self._cause = cause
        super().__init__(message=message, cause=cause)


class SizeMistmatchError(AtbuException):
    def __init__(self, message: str = None, cause=None):
        self._cause = cause
        super().__init__(message=message, cause=cause)


class DateTimeMistmatchError(AtbuException):
    def __init__(self, message: str = None, cause=None):
        self._cause = cause
        super().__init__(message=message, cause=cause)


class DigestMistmatchError(AtbuException):
    def __init__(self, message: str = None, cause=None):
        self._cause = cause
        super().__init__(message=message, cause=cause)


class CompareBytesMistmatchError(AtbuException):
    def __init__(self, message: str = None, cause=None):
        self._cause = cause
        super().__init__(message=message, cause=cause)


class AlreadyFinalizedError(AtbuException):
    def __init__(self, message: str = None, cause=None):
        self._cause = cause
        super().__init__(message=message, cause=cause)


class AlreadyUsedError(AtbuException):
    def __init__(self, message: str = None, cause=None):
        self._cause = cause
        super().__init__(message=message, cause=cause)


class EncryptionDecryptionFailure(AtbuException):
    def __init__(self, message: str = None, cause=None):
        self._cause = cause
        super().__init__(message=message, cause=cause)


class StateNotYetKnownError(AtbuException):
    def __init__(self, message: str = None, cause=None):
        self._cause = cause
        super().__init__(message=message, cause=cause)


class InvalidCommandLineArgument(AtbuException):
    def __init__(self, message: str = None, cause=None):
        self._cause = cause
        super().__init__(message=message, cause=cause)


class InvalidFunctionArgument(AtbuException):
    def __init__(self, message: str = None, cause=None):
        self._cause = cause
        super().__init__(message=message, cause=cause)


class InvalidBase64StringError(AtbuException):
    def __init__(self, message: str = None, cause=None):
        self._cause = cause
        super().__init__(message=message, cause=cause)


class LockError(AtbuException):
    def __init__(self, message: str = None, cause=None):
        super().__init__(message=message, cause=cause)


def exc_to_string(ex: Exception):
    return f"ex={ex} details: {traceback.format_exception(ex, ex, ex.__traceback__)}"


def exc_to_string_with_newlines(ex: Exception):
    traceback_list = traceback.format_exception(ex, ex, ex.__traceback__)
    traceback_str = "".join(traceback_list)
    return f"ex={ex} details: {traceback_str}"


def cur_exc_to_string():
    ex = sys.exc_info()[1]
    if ex is None:
        return "ex=<NoneType>"
    return exc_to_string(ex)
