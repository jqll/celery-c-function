// Copyright 2018 Google LLC
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      https://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#include <Python.h>
#include <unistd.h>


namespace {
PyObject* LongSleep(PyObject* self, PyObject* args) {

  // Releases GIL.
  Py_BEGIN_ALLOW_THREADS;

  sleep(20);

  // Reacquire the GIL.
  Py_END_ALLOW_THREADS;
  Py_INCREF(Py_None);
  return Py_None;
}

PyMethodDef Methods[] = {
    {"long_sleep", LongSleep, METH_VARARGS, "A function that sleeps for 20s."},
    {nullptr, nullptr, 0, nullptr} /* Sentinel */
};


struct PyModuleDef moduledef = {
    PyModuleDef_HEAD_INIT, "longsleep",           /* name of module */
    "", /* module documentation */
    -1, Methods};
}  // namespace

PyMODINIT_FUNC PyInit_longsleep(void) { return PyModule_Create(&moduledef); }







