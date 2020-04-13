#include "extcode.h"
#pragma pack(push)
#pragma pack(1)

#ifdef __cplusplus
extern "C" {
#endif
typedef struct {
	int32_t dimSizes[2];
	double elt[1];
} DoubleArrayBase;
typedef DoubleArrayBase **DoubleArray;

/*!
 * GettingStarted_5775_Host_Basic_pn_SH
 */
int32_t __cdecl GettingStarted_5775_Host_Basic_pn_SH(LStrHandle *RIODevice, 
	char AIChannels[], uint64_t AINumSamples, DoubleArray *WaveformGraph, 
	double *dt);

MgErr __cdecl LVDLLStatus(char *errStr, int errStrLen, void *module);

/*
* Memory Allocation/Resize/Deallocation APIs for type 'DoubleArray'
*/
DoubleArray __cdecl AllocateDoubleArray (int32 *dimSizeArr);
MgErr __cdecl ResizeDoubleArray (DoubleArray *hdlPtr, int32 *dimSizeArr);
MgErr __cdecl DeAllocateDoubleArray (DoubleArray *hdlPtr);

void __cdecl SetExecuteVIsInPrivateExecutionSystem(Bool32 value);

#ifdef __cplusplus
} // extern "C"
#endif

#pragma pack(pop)

