import json

# Taxonomy IDs mapped from your skills.csv sample
# I have linked these logically to your job titles (e.g., Python Developer -> Haskell ID)
skill_ids = {
    "tech": "362e9021-c661-4f0b-a6ad-13c418064c68",      # Haskell (Tech Proxy)
    "med": "4d086005-8c68-42a3-aa59-dacd0e4634df",       # Anti-oppressive practices
    "sales": "0630f6e4-cc30-4c77-811c-f0869f927cbc",     # Diplomatic principles
    "design": "1592e0e5-b022-403f-8dc1-d2409a8cc3ce",    # Work with soloists
    "edu": "0ec034d1-d1c4-423d-aa0b-a0f70cc4019f",       # Teach housekeeping
    "fin": "ef8c4daf-f518-438a-9cc2-afeea2f720d1",       # Risk management
    "hosp": "0223c3bb-47e0-4599-a5a0-daf658aa0fea",      # Food waste reduction
    "admin": "aeb18720-84f5-48e0-b101-4166e7d45049",     # Identify available services
    "sec": "90c120b4-3e26-4879-b914-b7f04b59fcd5",       # Lead investigations
    "agri": "bba41e33-2d29-4794-b7a8-ae7e9e8e5f7c",      # Maintain aquaculture
    "manuf": "7311619a-25b9-44c3-bc7c-1597a36e41b8",     # Handle equipment
}

# Skill Groups from your hierarchy snippet
group_ids = ["68933870ba407998dac8a042", "68933870ba407998dac8a0d0", 
             "68933870ba407998dac8a248", "68933870ba407998dac8a1a9"]

# --- 1. GENERATE DEMAND (20 Original Jobs + Skill Injection) ---
raw_demand = [
    {"uuid": "job_001", "originUuid": "tech_01", "opportunity_title": "Senior Python Developer", "location": "Remote", "contract_type": "full_time", "attributes": {"earnings_per_month": "earn_70k", "task_content": "task_creative", "physical_demand": "phys_light", "work_flexibility": "flex_high", "social_interaction": "soc_alone", "career_growth": "growth_high", "social_meaning": "mean_low", "expected_demand": "Very Low Expected Demand"}, "essential": [skill_ids["tech"]], "group": group_ids[0]},
    {"uuid": "job_003", "originUuid": "med_01", "opportunity_title": "Community Health Nurse", "location": "Kisumu", "contract_type": "full_time", "attributes": {"earnings_per_month": "earn_30k", "task_content": "task_mix", "physical_demand": "phys_light", "work_flexibility": "flex_some", "social_interaction": "soc_people", "career_growth": "growth_high", "social_meaning": "mean_high", "expected_demand": "Very Low Expected Demand"}, "essential": [skill_ids["med"]], "group": group_ids[2]},
    {"uuid": "job_004", "originUuid": "sales_01", "opportunity_title": "Regional Sales Manager", "location": "Mombasa", "contract_type": "full_time", "attributes": {"earnings_per_month": "earn_70k", "task_content": "task_mix", "physical_demand": "phys_light", "work_flexibility": "flex_some", "social_interaction": "soc_people", "career_growth": "growth_high", "social_meaning": "mean_low", "expected_demand": "High Expected Demand"}, "essential": [skill_ids["sales"]], "group": group_ids[3]},
    {"uuid": "job_005", "originUuid": "design_01", "opportunity_title": "Freelance Graphic Designer", "location": "Remote", "contract_type": "freelance", "attributes": {"earnings_per_month": "earn_30k", "task_content": "task_creative", "physical_demand": "phys_light", "work_flexibility": "flex_high", "social_interaction": "soc_alone", "career_growth": "growth_med", "social_meaning": "mean_high", "expected_demand": "Very Low Expected Demand"}, "essential": [skill_ids["design"]], "group": group_ids[0]},
    {"uuid": "job_007", "originUuid": "edu_01", "opportunity_title": "Primary School Teacher", "location": "Eldoret", "contract_type": "full_time", "attributes": {"earnings_per_month": "earn_30k", "task_content": "task_routine", "physical_demand": "phys_light", "work_flexibility": "flex_fixed", "social_interaction": "soc_people", "career_growth": "growth_med", "social_meaning": "mean_high", "expected_demand": "High Expected Demand"}, "essential": [skill_ids["edu"]], "group": group_ids[2]},
    {"uuid": "job_008", "originUuid": "fin_01", "opportunity_title": "Junior Accountant", "location": "Nairobi", "contract_type": "internship", "attributes": {"earnings_per_month": "earn_30k", "task_content": "task_routine", "physical_demand": "phys_light", "work_flexibility": "flex_fixed", "social_interaction": "soc_alone", "career_growth": "growth_high", "social_meaning": "mean_low", "expected_demand": "Moderate Expected Demand"}, "essential": [skill_ids["fin"]], "group": group_ids[3]},
    {"uuid": "job_009", "originUuid": "tech_02", "opportunity_title": "Electrician Assistant", "location": "Thika", "contract_type": "contract", "attributes": {"earnings_per_month": "earn_30k", "task_content": "task_mix", "physical_demand": "phys_heavy", "work_flexibility": "flex_some", "social_interaction": "soc_people", "career_growth": "growth_med", "social_meaning": "mean_low", "expected_demand": "Very Low Expected Demand"}, "essential": [skill_ids["tech"]], "group": group_ids[0]},
    {"uuid": "job_010", "originUuid": "hosp_01", "opportunity_title": "Line Cook", "location": "Nairobi", "contract_type": "full_time", "attributes": {"earnings_per_month": "earn_30k", "task_content": "task_creative", "physical_demand": "phys_heavy", "work_flexibility": "flex_fixed", "social_interaction": "soc_people", "career_growth": "growth_med", "social_meaning": "mean_low", "expected_demand": "Very Low Expected Demand"}, "essential": [skill_ids["hosp"]], "group": group_ids[1]},
    {"uuid": "job_011", "originUuid": "admin_01", "opportunity_title": "Data Entry Clerk", "location": "Remote", "contract_type": "part_time", "attributes": {"earnings_per_month": "earn_15k", "task_content": "task_routine", "physical_demand": "phys_light", "work_flexibility": "flex_high", "social_interaction": "soc_alone", "career_growth": "growth_low", "social_meaning": "mean_low", "expected_demand": "Low Expected Demand"}, "essential": [skill_ids["admin"]], "group": group_ids[2]},
    {"uuid": "job_012", "originUuid": "sec_01", "opportunity_title": "Night Guard", "location": "Nairobi", "contract_type": "full_time", "attributes": {"earnings_per_month": "earn_15k", "task_content": "task_routine", "physical_demand": "phys_light", "work_flexibility": "flex_fixed", "social_interaction": "soc_alone", "career_growth": "growth_low", "social_meaning": "mean_high", "expected_demand": "Low Expected Demand"}, "essential": [skill_ids["sec"]], "group": group_ids[3]},
    {"uuid": "job_013", "originUuid": "agri_01", "opportunity_title": "Farm Hand", "location": "Naivasha", "contract_type": "seasonal", "attributes": {"earnings_per_month": "earn_15k", "task_content": "task_routine", "physical_demand": "phys_heavy", "work_flexibility": "flex_some", "social_interaction": "soc_alone", "career_growth": "growth_low", "social_meaning": "mean_high", "expected_demand": "Moderate Expected Demand"}, "essential": [skill_ids["agri"]], "group": group_ids[0]},
    {"uuid": "job_015", "originUuid": "serv_01", "opportunity_title": "Call Center Agent", "location": "Nairobi", "contract_type": "full_time", "attributes": {"earnings_per_month": "earn_30k", "task_content": "task_routine", "physical_demand": "phys_light", "work_flexibility": "flex_fixed", "social_interaction": "soc_people", "career_growth": "growth_med", "social_meaning": "mean_low", "expected_demand": "Moderate Expected Demand"}, "essential": [skill_ids["admin"]], "group": group_ids[2]},
    {"uuid": "job_016", "originUuid": "tech_03", "opportunity_title": "Frontend Developer", "location": "Remote", "contract_type": "contract", "attributes": {"earnings_per_month": "earn_70k", "task_content": "task_creative", "physical_demand": "phys_light", "work_flexibility": "flex_high", "social_interaction": "soc_alone", "career_growth": "growth_high", "social_meaning": "mean_low", "expected_demand": "Very Low Expected Demand"}, "essential": [skill_ids["tech"]], "group": group_ids[3]},
    {"uuid": "job_018", "originUuid": "man_01", "opportunity_title": "Factory Machine Operator", "location": "Industrial Area", "contract_type": "full_time", "attributes": {"earnings_per_month": "earn_30k", "task_content": "task_routine", "physical_demand": "phys_heavy", "work_flexibility": "flex_fixed", "social_interaction": "soc_alone", "career_growth": "growth_low", "social_meaning": "mean_low", "expected_demand": "Moderate Expected Demand"}, "essential": [skill_ids["manuf"]], "group": group_ids[1]},
   
]

# --- 2. FORMAT AND SAVE DEMAND.JSONL ---
with open('demand.jsonl', 'w') as f:
    for item in raw_demand:
        # We inject the new scoring fields while keeping original location and attributes
        record = {
            "uuid": item["uuid"],
            "originUuid": item["originUuid"],
            "opportunity_title": item["opportunity_title"],
            "location": item["location"],
            "city": item["location"], # Helper for U_loc
            "province": item["location"], # Helper for U_loc
            "contract_type": item["contract_type"],
            "essential_skills_origin_uuids": item["essential"],
            "optional_skills_origin_uuids": [],
            "skill_groups_origin_uuids": [item["group"]],
            "attributes": item["attributes"]
        }
        f.write(json.dumps(record) + '\n')

print("Success: demand.jsonl generated with all original attributes + matching UUIDs.")