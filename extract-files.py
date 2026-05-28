#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)

from extract_utils.fixups_lib import (
    lib_fixup_remove,
    lib_fixups,
    lib_fixups_user_type,
)

from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    "device/motorola/sm6450-common",
    "hardware/motorola",
    "hardware/qcom-caf/sm8450-6.6",
    "hardware/qcom-caf/wlan",
    "vendor/qcom/opensource/commonsys/display",
    "vendor/qcom/opensource/commonsys-intf/display",
    "vendor/qcom/opensource/dataservices",
]

libs_add_vendor_suffix = (
    "com.qualcomm.qti.dpm.api@1.0",
    "vendor.qti.ImsRtpService-V1-ndk",
    "vendor.qti.diaghal-V1-ndk",
    "vendor.qti.hardware.dpmaidlservice-V1-ndk",
    "vendor.qti.qccsyshal_aidl-V1-ndk",
    "vendor.qti.qccvndhal_aidl-V1-ndk",
)

def lib_fixup_vendor_suffix(lib: str, partition: str, *args, **kwargs):
    if partition != "vendor":
        return None

    return f"{lib}_{partition}"


lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
    libs_add_vendor_suffix: lib_fixup_vendor_suffix,
}

blob_fixups: blob_fixups_user_type = {
}  # fmt: skip

module = ExtractUtilsModule(
    "sm6450-common",
    "motorola",
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
)

if __name__ == "__main__":
    utils = ExtractUtils.device(module)
    utils.run()
