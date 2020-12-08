// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

// Export members:
export * from "./account";
export * from "./accountNetworkRules";
export * from "./blob";
export * from "./container";
export * from "./customerManagedKey";
export * from "./dataLakeGen2Filesystem";
export * from "./dataLakeGen2Path";
export * from "./encryptionScope";
export * from "./getAccount";
export * from "./getAccountBlobContainerSAS";
export * from "./getAccountSAS";
export * from "./getEncryptionScope";
export * from "./getPolicy";
export * from "./getStorageContainer";
export * from "./getSync";
export * from "./getSyncGroup";
export * from "./managementPolicy";
export * from "./queue";
export * from "./share";
export * from "./shareDirectory";
export * from "./sync";
export * from "./syncGroup";
export * from "./table";
export * from "./tableEntity";
export * from "./zMixins";
export * from "./zipBlob";

// Import resources to register:
import { Account } from "./account";
import { AccountNetworkRules } from "./accountNetworkRules";
import { Blob } from "./blob";
import { Container } from "./container";
import { CustomerManagedKey } from "./customerManagedKey";
import { DataLakeGen2Filesystem } from "./dataLakeGen2Filesystem";
import { DataLakeGen2Path } from "./dataLakeGen2Path";
import { EncryptionScope } from "./encryptionScope";
import { ManagementPolicy } from "./managementPolicy";
import { Queue } from "./queue";
import { Share } from "./share";
import { ShareDirectory } from "./shareDirectory";
import { Sync } from "./sync";
import { SyncGroup } from "./syncGroup";
import { Table } from "./table";
import { TableEntity } from "./tableEntity";
import { ZipBlob } from "./zipBlob";

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "azure:storage/account:Account":
                return new Account(name, <any>undefined, { urn })
            case "azure:storage/accountNetworkRules:AccountNetworkRules":
                return new AccountNetworkRules(name, <any>undefined, { urn })
            case "azure:storage/blob:Blob":
                return new Blob(name, <any>undefined, { urn })
            case "azure:storage/container:Container":
                return new Container(name, <any>undefined, { urn })
            case "azure:storage/customerManagedKey:CustomerManagedKey":
                return new CustomerManagedKey(name, <any>undefined, { urn })
            case "azure:storage/dataLakeGen2Filesystem:DataLakeGen2Filesystem":
                return new DataLakeGen2Filesystem(name, <any>undefined, { urn })
            case "azure:storage/dataLakeGen2Path:DataLakeGen2Path":
                return new DataLakeGen2Path(name, <any>undefined, { urn })
            case "azure:storage/encryptionScope:EncryptionScope":
                return new EncryptionScope(name, <any>undefined, { urn })
            case "azure:storage/managementPolicy:ManagementPolicy":
                return new ManagementPolicy(name, <any>undefined, { urn })
            case "azure:storage/queue:Queue":
                return new Queue(name, <any>undefined, { urn })
            case "azure:storage/share:Share":
                return new Share(name, <any>undefined, { urn })
            case "azure:storage/shareDirectory:ShareDirectory":
                return new ShareDirectory(name, <any>undefined, { urn })
            case "azure:storage/sync:Sync":
                return new Sync(name, <any>undefined, { urn })
            case "azure:storage/syncGroup:SyncGroup":
                return new SyncGroup(name, <any>undefined, { urn })
            case "azure:storage/table:Table":
                return new Table(name, <any>undefined, { urn })
            case "azure:storage/tableEntity:TableEntity":
                return new TableEntity(name, <any>undefined, { urn })
            case "azure:storage/zipBlob:ZipBlob":
                return new ZipBlob(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("azure", "storage/account", _module)
pulumi.runtime.registerResourceModule("azure", "storage/accountNetworkRules", _module)
pulumi.runtime.registerResourceModule("azure", "storage/blob", _module)
pulumi.runtime.registerResourceModule("azure", "storage/container", _module)
pulumi.runtime.registerResourceModule("azure", "storage/customerManagedKey", _module)
pulumi.runtime.registerResourceModule("azure", "storage/dataLakeGen2Filesystem", _module)
pulumi.runtime.registerResourceModule("azure", "storage/dataLakeGen2Path", _module)
pulumi.runtime.registerResourceModule("azure", "storage/encryptionScope", _module)
pulumi.runtime.registerResourceModule("azure", "storage/managementPolicy", _module)
pulumi.runtime.registerResourceModule("azure", "storage/queue", _module)
pulumi.runtime.registerResourceModule("azure", "storage/share", _module)
pulumi.runtime.registerResourceModule("azure", "storage/shareDirectory", _module)
pulumi.runtime.registerResourceModule("azure", "storage/sync", _module)
pulumi.runtime.registerResourceModule("azure", "storage/syncGroup", _module)
pulumi.runtime.registerResourceModule("azure", "storage/table", _module)
pulumi.runtime.registerResourceModule("azure", "storage/tableEntity", _module)
pulumi.runtime.registerResourceModule("azure", "storage/zipBlob", _module)
