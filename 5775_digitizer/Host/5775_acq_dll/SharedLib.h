#include "extcode.h"
#pragma pack(push)
#pragma pack(1)

#ifdef __cplusplus
extern "C" {
#endif

/*!
 * GettingStarted_5775_Host_Basic_pn_SH
 */
int32_t __cdecl GettingStarted_5775_Host_Basic_pn_SH(char BitFilePath[], 
	char DeviceId[], char AIChannels[], uint64_t AINumSamples, 
	double FirstChannel[], int32_t len, double SecondChannel[], int32_t len2, 
	double *dt);

MgErr __cdecl LVDLLStatus(char *errStr, int errStrLen, void *module);

void __cdecl SetExecuteVIsInPrivateExecutionSystem(Bool32 value);

#ifdef __cplusplus
} // extern "C"
#endif

#pragma pack(pop)

