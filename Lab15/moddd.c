#include <Python.h>
#include "funkcja.h"
//mozliwe sygnatury funkcji stanowiącej "interfejs" pomiędzy pythonem i C
//static PyObject *moddd_met(PyObject *self){
//static PyObject *moddd_met(PyObject *self, PyObject *args, PyObject *kw){

static PyObject *moddd_met(PyObject *self, PyObject *args){
	int a,b;
	int c=0;
	PyObject *d=NULL;
	if(!PyArg_ParseTuple(args, "ii|iO", &a, &b, &c, &d)){ //jezeli do stringa wstawi sie | to po sa parametry opcjonalne; O od Object
		return NULL;	//zwracane w przypadku bledu; interpreter zglasza wyjatek wywolania funkcji
	}
	int s=a+b+c;
	if(d){
		int r=PyList_Size(d);
		for(int i=0; i<r; i++){
			s+=PyLong_AsLong(PyList_GetItem(d,i));
		}
	}
	//Py_RETURN_NONE; //jesli nic nie zwraca
	return Py_BuildValue("i", s);
}

static PyObject *moddd_sort(PyObject *self, PyObject *args){
	PyObject *Tab=NULL;
	if(!PyArg_ParseTuple(args, "O", &Tab)){ //jezeli do stringa wstawi sie | to po sa parametry opcjonalne; O od Object
		return NULL;	//zwracane w przypadku bledu; interpreter zglasza wyjatek wywolania funkcji
	}
  int size=PyList_Size(Tab);
	int *tab=(int*)malloc(sizeof(int)*size);
	for(int i=0;i<size;i++)
  {
    tab[i]=PyLong_AsLong(PyList_GetItem(Tab,i));
  }
  // insert_sort(tab,size);
  for(int i=0;i<size;i++)
  {
    PyList_SetItem(Tab,i,PyLong_FromLong(tab[i]));
  }
	//Py_RETURN_NONE; //jesli nic nie zwraca
  free(tab);
	return Py_BuildValue("O", Tab);
}

static PyObject *moddd_NWD(PyObject *self, PyObject *args){
	PyObject *Dic=NULL;
	if(!PyArg_ParseTuple(args, "O", &Dic)){ //jezeli do stringa wstawi sie | to po sa parametry opcjonalne; O od Object
		return NULL;	//zwracane w przypadku bledu; interpreter zglasza wyjatek wywolania funkcji
	}
	PyObject* output =PyDict_New();
  PyObject* key,*val;
  Py_ssize_t p=0;
  while(PyDict_Next(Dic,&p,&key,&val))
  {
    int temp=nwd(PyLong_AsLong(key),PyLong_AsLong(val));
    PyObject* cos =PyTuple_New(2);
    PyTuple_SetItem(cos,0,key);
    PyTuple_SetItem(cos,1,val);
    PyDict_SetItem(output,cos,PyLong_FromLong(temp));
  }
  return Py_BuildValue("O",output);
}


//tablica metod
static PyMethodDef moddd_metody[]={
	{"met", (PyCFunction)moddd_met, METH_VARARGS, "Funkcja ..."},
  {"sort", (PyCFunction)moddd_sort, METH_VARARGS, "Funkcja ..."},
  {"NWD", (PyCFunction)moddd_NWD, METH_VARARGS, "Funkcja ..."}, 
	//nazwa funkcja stosowana w Pythonie, adres funkcji , j.w. lub METH_KEYWORDS lub METH_NOARGS, lancuch dokumentacyjny
	{NULL, NULL, 0, NULL}	//wartownik
};


static struct PyModuleDef module={
        PyModuleDef_HEAD_INIT,
        "moddd",
        NULL,
        -1,
        moddd_metody
};

//funkcja inicjalizujaca
PyMODINIT_FUNC PyInit_moddd(void){
        return PyModule_Create(&module);
}
