BASE_PATH = "/Volumes/workspace/bronze/source_systems"

INGESTION_CONFIG = [
    # CRM
    {
        "source": "source_crm",
        "path": f"{BASE_PATH}/source_crm/cust_info.csv",
        "table": "crm_cust_info_raw.csv"
    },
    {
        "source": "source_crm",
        "path": f"{BASE_PATH}/source_crm/prd_info.csv",
        "table": "crm_prd_info_raw.csv"
    },
    {
        "source": "source_crm",
        "path": f"{BASE_PATH}/source_crm/sales_details.csv",
        "table": "sales_details_raw.csv"
    },

    # ERP
    {
        "source": "source_erp",
        "path": f"{BASE_PATH}/source_erp/CUST_AZ12.csv",
        "table": "erp_cust_az12_raw.csv"
    },
    {
        "source": "source_erp",
        "path": f"{BASE_PATH}/source_erp/LOC_A101.csv",
        "table": "erp_loc_a101_raw.csv"
    },
    {
        "source": "source_erp",
        "path": f"{BASE_PATH}/source_erp/PX_CAT_G1V2.csv",
        "table": "erp_px_cat_g1v2_raw.csv"
    },
]