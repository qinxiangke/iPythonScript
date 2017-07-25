import sys
import os
#line='[MISRA 2012 Rule 2.2, required]'
#calculate how many the key happens in the specific file
def countKeyInFile(key,file):
    with open(file, 'r') as f:
        lines = f.readlines()    
        num=0
        for line in lines:
            length=len(line)
            num+=line.count(key,0,length)
    return num

#os.remove(sys.argv[1])
keyList=["Directive 1.1,", "Directive 2.1,", "Directive 3.2,", "Directive 4.1,", "Directive 4.2,", "Directive 4.3,", "Directive 4.4,", "Directive 4.5,", "Directive 4.6,", "Directive 4.7,", "Directive 4.8,", "Directive 4.9,", "Directive 4.10,", "Directive 4.11,", "Directive 4.12,", "Directive 4.13,", "Rule 1.1,", "Rule 1.2,", "Rule 1.3,", "Rule 2.1,", "Rule 2.2,", "Rule 2.3,", "Rule 2.4,", "Rule 2.5,", "Rule 2.6,", "Rule 2.7,", "Rule 3.1,", "Rule 3.2,", "Rule 4.1,", "Rule 4.2,", "Rule 5.1,", "Rule 5.2,", "Rule 5.3,", "Rule 5.4,", "Rule 5.5,", "Rule 5.6,", "Rule 5.7,", "Rule 5.8,", "Rule 5.9,", "Rule 6.1,", "Rule 6.2,", "Rule 7.1,", "Rule 7.2,", "Rule 7.3,", "Rule 7.4,", "Rule 8.1,", "Rule 8.2,", "Rule 8.3,", "Rule 8.4,", "Rule 8.5,", "Rule 8.6,", "Rule 8.7,", "Rule 8.8,", "Rule 8.9,", "Rule 8.10,", "Rule 8.11,", "Rule 8.12,", "Rule 8.13,", "Rule 8.14,", "Rule 9.1,", "Rule 9.2,", "Rule 9.3,", "Rule 9.4,", "Rule 9.5,", "Rule 10.1,", "Rule 10.2,", "Rule 10.3,", "Rule 10.4,", "Rule 10.5,", "Rule 10.6,", "Rule 10.7,", "Rule 10.8,", "Rule 11.1,", "Rule 11.2,", "Rule 11.3,", "Rule 11.4,", "Rule 11.5,", "Rule 11.6,", "Rule 11.7,", "Rule 11.8,", "Rule 11.9,", "Rule 12.1,", "Rule 12.2,", "Rule 12.3,", "Rule 12.4,", "Rule 13.1,", "Rule 13.2,", "Rule 13.3,", "Rule 13.4,", "Rule 13.5,", "Rule 13.6,", "Rule 14.1,", "Rule 14.2,", "Rule 14.3,", "Rule 14.4,", "Rule 15.1,", "Rule 15.2,", "Rule 15.3,", "Rule 15.4,", "Rule 15.5,", "Rule 15.6,", "Rule 15.7,", "Rule 16.1,", "Rule 16.2,", "Rule 16.3,", "Rule 16.4,", "Rule 16.5,", "Rule 16.6,", "Rule 16.7,", "Rule 17.1,", "Rule 17.2,", "Rule 17.3,", "Rule 17.4,", "Rule 17.5,", "Rule 17.6,", "Rule 17.7,", "Rule 17.8,", "Rule 18.1,", "Rule 18.2,", "Rule 18.3,", "Rule 18.4,", "Rule 18.5,", "Rule 18.6,", "Rule 18.7,", "Rule 18.8,", "Rule 19.1,", "Rule 19.2,", "Rule 20.1,", "Rule 20.2,", "Rule 20.3,", "Rule 20.4,", "Rule 20.5,", "Rule 20.6,", "Rule 20.7,", "Rule 20.8,", "Rule 20.9,", "Rule 20.10,", "Rule 20.11,", "Rule 20.12,", "Rule 20.13,", "Rule 20.14,", "Rule 21.1,", "Rule 21.2,", "Rule 21.3,", "Rule 21.4,", "Rule 21.5,", "Rule 21.6,", "Rule 21.7,", "Rule 21.8,", "Rule 21.9,", "Rule 21.10,", "Rule 21.11,", "Rule 21.12,", "Rule 22.1,", "Rule 22.2,", "Rule 22.3,", "Rule 22.4,", "Rule 22.5,", "Rule 22.6,"];
logFileList=["CSTATMEGA328PB_TU_TI.build.log","CSTRH850_TUTI.build.log","CSTRL78_TU_TI.build.log","DBATTERY_TU_TI.build.log","DDCM_TU_TI.build.log","DENC_TU_TI.build.log","DKEY_TU_TI.build.log","DOWD_TU_TI.build.log","DPOTI_T32_UT.build.log","DPROBE_T32_UT.build.log","DWDOG_TU_TI.build.log","global-build.log","LDBATTERY_TU_TI.build.log","LDEEP_TU_TI.build.log","LDKEY_TU_TI.build.log","LDWDOG_TU_TI.build.log","RAMT_TU_TI.build.log","ResetManagerTV.build.log","SCPULD_TV.build.log","SHYST_TU_TI.build.log","SLINEAR_TU_TI.build.log","SMEASURETIME_TU_TI.build.log","SSWt_TU_TI.build.log","_Kal000_tests.build.log","_Kal001_tests.build.log","_Kal002_tests.build.log"];
reportFileList=["CSTATMEGA328PB_TU_TI.build.rpt","CSTRH850_TUTI.build.rpt","CSTRL78_TU_TI.build.rpt","DBATTERY_TU_TI.build.rpt","DDCM_TU_TI.build.rpt","DENC_TU_TI.build.rpt","DKEY_TU_TI.build.rpt","DOWD_TU_TI.build.rpt","DPOTI_T32_UT.build.rpt","DPROBE_T32_UT.build.rpt","DWDOG_TU_TI.build.rpt","global-build.rpt","LDBATTERY_TU_TI.build.rpt","LDEEP_TU_TI.build.rpt","LDKEY_TU_TI.build.rpt","LDWDOG_TU_TI.build.rpt","RAMT_TU_TI.build.rpt","ResetManagerTV.build.rpt","SCPULD_TV.build.rpt","SHYST_TU_TI.build.rpt","SLINEAR_TU_TI.build.rpt","SMEASURETIME_TU_TI.build.rpt","SSWt_TU_TI.build.rpt","_Kal000_tests.build.rpt","_Kal001_tests.build.rpt","_Kal002_tests.build.rpt"];

#the index as reportFileList
idx=0
for logFile in logFileList:
    sum=0
    print(idx)
    reportFile=reportFileList[idx]
    if os.path.isfile(reportFile):
        os.remove(reportFile)
    for key in keyList:
        counter=countKeyInFile(key,logFile)
        sum+=counter
    #    print(key,counter)
        with open(reportFile, 'a') as f:
    #        if counter != 0:
    #        f.write(key)
    #       f.write(':')
    #        f.write(logFile)
            f.write(str(counter))
            f.write('\n')
    idx+=1
