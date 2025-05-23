# Copyright 2019 Xanadu Quantum Technologies Inc.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Top level PennyLane-qiskit module"""

from ._version import __version__
from .aer import AerDevice
from .basic_sim import BasicSimulatorDevice
from .remote import RemoteDevice
from .converter import load, load_pauli_op, load_qasm, load_qasm_from_file, load_noise_model
from .qiskit_device import qiskit_session
