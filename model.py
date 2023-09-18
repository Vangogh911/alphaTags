ai_dt_params = ["iCmd", "iEUMax", "iEUMin", "iEUSim", "iLimAH", "iLimWH", "iLimWL", "iLimAL", "iRawValue", "qEU",
                "qStateHMI", "qMode"]
dx_dt_params = ["iIn", "iInv", "qOut", "iSim_En", "iSim_Value", "iTime_On", "iTime_Off"]


def ai_modules():
    with open("plc.xml", "a", encoding="utf-8") as code:
        for i in range(5):
            for j in range(16):
                for k in range(len(ai_dt_params)):
                    code.write(f'  <item Binding = "Introduced">\n')
                    code.write(f'    <node-path>PLC.AI.Module_{i+1}.AI{j+1}._AIPresets.{ai_dt_params[k]}</node-path>\n')
                    code.write(f'    <namespace>CODESYSSPV3/3S/IecVarAccess</namespace>\n')
                    code.write(f'    <nodeIdType>String</nodeIdType>\n')
                    code.write(f'    <nodeId>Application.DB_sig.AI.AI[{j+(i*16)}].{ai_dt_params[k]}</nodeId>\n')
                    code.write(f'  </item>\n')


def di_modules():
    with open("plc.xml", "a", encoding="utf-8") as code:
        for i in range(4):
            for j in range(32):
                for k in range(len(dx_dt_params)):
                    code.write(f'  <item Binding = "Introduced">\n')
                    if dx_dt_params[k] == "iTime_On" or dx_dt_params[k] == "iTime_Off":
                        code.write(f'    <node-path>PLC.DI.Module_{i+1}.DI{j+1}._DxTime.{dx_dt_params[k]}</node-path>\n')
                    else:
                        code.write(f'    <node-path>PLC.DI.Module_{i+1}.DI{j+1}._DxBits.{dx_dt_params[k]}</node-path>\n')
                    code.write(f'    <namespace>CODESYSSPV3/3S/IecVarAccess</namespace>\n')
                    code.write(f'    <nodeIdType>String</nodeIdType>\n')
                    code.write(f'    <nodeId>Application.DB_sig.DI.DI[{j+(i*32)}].{dx_dt_params[k]}</nodeId>\n')
                    code.write(f'  </item>\n')


def dq_modules():
    with open("plc.xml", "a", encoding="utf-8") as code:
        for i in range(3):
            for j in range(32):
                for k in range(len(dx_dt_params)):
                    code.write(f'  <item Binding = "Introduced">\n')
                    if dx_dt_params[k] == "iTime_On" or dx_dt_params[k] == "iTime_Off":
                        code.write(f'    <node-path>PLC.DQ.Module_{i+1}.DQ{j+1}._DxTime.{dx_dt_params[k]}</node-path>\n')
                    else:
                        code.write(f'    <node-path>PLC.DQ.Module_{i+1}.DQ{j+1}._DxBits.{dx_dt_params[k]}</node-path>\n')
                    code.write(f'    <namespace>CODESYSSPV3/3S/IecVarAccess</namespace>\n')
                    code.write(f'    <nodeIdType>String</nodeIdType>\n')
                    code.write(f'    <nodeId>Application.DB_sig.DQ.DQ[{j+(i*32)}].{dx_dt_params[k]}</nodeId>\n')
                    code.write(f'  </item>\n')


if __name__ == '__main__':
    with open("plc.xml", "a", encoding="utf-8") as c:
        c.write('<root format-version="0">\n')
    ai_modules()
    di_modules()
    dq_modules()
    with open("plc.xml", "a", encoding="utf-8") as c:
        c.write('</root>')
