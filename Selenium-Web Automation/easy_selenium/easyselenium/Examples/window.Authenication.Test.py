#This windlw_aler program will not work in browserless beacause of its sending keys to windows application throguh keyboard control

from easyselenium import *
import time
driver=open_browser(browser='firefox')
open_url('https://authiad2.apps.ocn.infra.ftgroup/login.php?timeout=14400')


window_alert(text="your login name")
{
    "config_type": "df",
    "parallelism": 20,
    "project_name": "acn-highmark-health-odh",
    "data_grooming_information": {
        "owner_name": "name",
        "owner_designation": "test",
        "owner_email": "name@email.com",
        "business_justification": "Required for testing"
    },
    "data_source": {
        "data_type": "CSV",
        "type_specific_details": {
            "provider_name": "GCP",
            "delimiter": ",",
            "escape_character": "\\",
            "header": "true",
            "source_path": "gs://odhtest-idf-dl-staging/staging/SCD1_ASAL.csv"
        }
    },
    "data_destination": [
        {
            "data_type": "DELTA",
            "type_specific_details": {
                "provider_name": "GCP",
                "destination_path": "gs://odhtest-idf-dl-curated/SCD1_ASAL/Delta/"
            }
        }
    ],
	"data_postgres": {
        "data_type": "delta",
        "type_specific_details": {
            "primary_keys" : "asal_id",
			"table_name": "scd1_asal",
            "database": "postgres",
            "schema_name": "postgresdev",
			"merge_type" : "scd1",
            "source_path": "gs://odhtest-idf-dl-curated/SCD1_ASAL/Delta/20211001105627"
        }
    },
    "raw_path": "gs://odhtest-idf-dl-raw/databricks",
    "quarantine_path": "gs://odhtest-idf-dl-quarentine/databricks_csv",
    "report_path": "gs://odhtest-idf-dl-report/databricks_csv",
    "rules_engine": {
        "predefined_rules": [],
        "expression_rules": [],
        "complex_rules": [],
        "direct_mapping": {},
        "derived_mapping": [],
        "filter_mapping": [],
        "generate_record_timestamp": false,
        "drop_empty_rows": {
            "enable": false
        }
    },
    "schema": [
        {
            "name": "ASAL_ID",
            "type": "long",
            "nullable": false,
            "metadata": {
                "iskey": true,
                "alias_name": "",
                "business_glossery": "",
                "description": ""
            }
        },
        {
            "name": "ASAL_TRAN_TYP_C",
            "type": "string",
            "nullable": false,
            "metadata": {
                "iskey": true,
                "alias_name": "",
                "business_glossery": "",
                "description": ""
            }
        },
        {
            "name": "ASAL_TBL_NM",
            "type": "string",
            "nullable": false,
            "metadata": {
                "iskey": false,
                "alias_name": "",
                "business_glossery": "",
                "description": ""
            }
        },
        {
            "name": "CL_ID",
            "type": "long",
            "nullable": true,
            "metadata": {
                "iskey": false,
                "alias_name": "",
                "business_glossery": "",
                "description": ""
            }
        },
        {
            "name": "ASAL_BFR_TBLREC_ID",
            "type": "long",
            "nullable": true,
            "metadata": {
                "iskey": false,
                "alias_name": "",
                "business_glossery": "",
                "description": ""
            }
        },
        {
            "name": "ASAL_AFT_TBLREC_ID",
            "type": "long",
            "nullable": false,
            "metadata": {
                "iskey": false,
                "alias_name": "",
                "business_glossery": "",
                "description": ""
            }
        },
        {
            "name": "ASAL_AFT_TBLSTUS_C",
            "type": "string",
            "nullable": true,
            "metadata": {
                "iskey": false,
                "alias_name": "",
                "business_glossery": "",
                "description": ""
            }
        },
        {
            "name": "ASAL_REC_MTN_TS",
            "type": "string",
            "nullable": false,
            "metadata": {
                "iskey": false,
                "alias_name": "",
                "business_glossery": "",
                "description": ""
            }
        },
        {
            "name": "ASAL_REC_MTN_ID",
            "type": "string",
            "nullable": false,
            "metadata": {
                "iskey": false,
                "alias_name": "",
                "business_glossery": "",
                "description": ""
            }
        },
        {
            "name": "ASAL_BFR_TBLSTUS_C",
            "type": "string",
            "nullable": true,
            "metadata": {
                "iskey": false,
                "alias_name": "",
                "business_glossery": "",
                "description": ""
            }
        },
        {
            "name": "RECORD_OPERATOR",
            "type": "string",
            "nullable": true,
            "metadata": {
                "iskey": false,
                "alias_name": "",
                "business_glossery": "",
                "description": ""
            }
        }
    ],
    "schema_validation": false,
    "schema_conversion": false,
    "data_quality": {
        "report_type": "JSON",
        "dataset_based_rules": {
            "assertion_rules": [],
            "sql_rules": [],
            "expression_rules": [],
            "complex_rules": []
        },
        "row_based_rules": {}
    }
}window_alert(text="your passsword",with_enter=True)