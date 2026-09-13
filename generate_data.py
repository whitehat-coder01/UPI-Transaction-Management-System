import random
from datetime import datetime, timedelta

# ============================================
# CONFIGURATION
# ============================================
NUM_USERS = 1000
NUM_TRANSACTIONS = 10000
OUTPUT_FILE = "database/seed_data_large.sql"

# ============================================
# REALISTIC INDIAN DATA POOLS
# ============================================
FIRST_NAMES = [
    "Harsh","Khushi","Komal","Ishan","Krunal","Hansal","Harshavardhan","Ayaan",
    "Krishna","Ishaan","Shaurya","Atharva","Advik","Pranav","Dhruv",
    "Kabir","Ritvik","Aarush","Kian","Darsh","Veer","Yuvraj","Ananya",
    "Diya","Anika","Saanvi","Aadhya","Isha","Myra","Sara","Aarohi",
    "Anvi","Kiara","Riya","Navya","Avni","Pari","Anaya","Kavya","Meera",
    "Rahul","Priya","Amit","Sneha","Vikram","Neha","Rohan","Pooja",
    "Karan","Divya","Arnav","Tanvi","Ishan","Ritika","Varun","Simran",
    "Manish","Kriti","Saurabh","Nidhi","Deepak","Swati","Nikhil","Megha",
    "Gaurav","Shruti","Harsh","Pallavi","Tarun","Vandana","Akash","Rashmi",
    "Mohit","Sakshi","Pankaj","Garima","Sandeep","Rekha","Vishal","Komal",
    "Rajesh","Anjali","Suresh","Kavita","Mukesh","Sunita","Ramesh","Preeti"
]

LAST_NAMES = [
    "Sharma","Patel","Kumar","Singh","Gupta","Reddy","Verma","Joshi",
    "Mishra","Chauhan","Agarwal","Yadav","Saxena","Mehta","Nair",
    "Iyer","Rao","Das","Bose","Sen","Mukherjee","Chatterjee","Banerjee",
    "Ganguly","Roy","Sinha","Pandey","Dubey","Tiwari","Shukla",
    "Malhotra","Kapoor","Khanna","Bhatia","Arora","Sethi","Chopra",
    "Menon","Pillai","Nambiar","Kulkarni","Deshpande","Patil","Jadhav",
    "More","Gaikwad","Shinde","Pawar","Kadam","Salunkhe"
]

BANKS = [
    ("State Bank of India",      "SBIN"),
    ("HDFC Bank",                "HDFC"),
    ("ICICI Bank",               "ICIC"),
    ("Axis Bank",                "UTIB"),
    ("Kotak Mahindra Bank",      "KKBK"),
    ("Punjab National Bank",     "PUNB"),
    ("Bank of Baroda",           "BARB"),
    ("Canara Bank",              "CNRB"),
    ("Union Bank of India",      "UBIN"),
    ("IDBI Bank",                "IBKL"),
    ("Yes Bank",                 "YESB"),
    ("IndusInd Bank",            "INDB"),
    ("Federal Bank",             "FDRL"),
    ("Bandhan Bank",             "BDBL"),
    ("Indian Bank",              "IDIB"),
]

UPI_HANDLES = ["@ybl","@oksbi","@okhdfcbank","@okicici","@okaxis",
               "@paytm","@apl","@ibl","@axl","@sbi","@hdfc","@icici",
               "@kotak","@pnb","@boi","@ubi","@freecharge"]

TXN_REMARKS = [
    "Lunch","Dinner","Groceries","Milk","Vegetables","Recharge",
    "Electricity Bill","Water Bill","Rent","EMI","Petrol","Uber",
    "Ola","Swiggy","Zomato","Amazon","Flipkart","Netflix","Hotstar",
    "PhonePe","School Fee","Medical","Medicine","Gym","Movie Ticket",
    "BookMyShow","Parking","Toll","Chai","Snacks","Birthday Gift",
    "Festival Gift","Diwali","Holi","Rakhi","Wedding Gift","Donation",
    "Temple","Church","Mosque","Tuition Fee","Stationery","Laundry",
    "Salon","Haircut","Courier","Post Office","Insurance","Mutual Fund",
    "SIP","Stock","Crypto","Gas Bill","Broadband","WiFi","DTH",
    "Mobile Bill","Credit Card","Loan","Interest","Salary","Freelance",
    "Consulting","Design","Development","Maintenance","Repair","Plumbing",
    "Electrician","Carpenter","Painting","Housekeeping","Maid","Driver",
    "Security","Watchman","Gardener","Cook","Tiffin Service","Catering",
    "Party","Restaurant","Cafe","Bar","Club","Concert","Festival",
    "Travel","Hotel","Flight","Train","Bus","Auto","Metro","Cab",
    "Shopping","Clothes","Shoes","Electronics","Phone","Laptop","Tablet",
    "Headphones","Speaker","Camera","Watch","Jewelry","Gold","Silver",
    "Furniture","Appliance","AC","Fridge","Washing Machine","TV",
    "Microwave","Oven","Mixer","Iron","Vacuum","Water Purifier"
]

# ============================================
# HELPER FUNCTIONS
# ============================================
def random_name():
    return f"{random.choice(FIRST_NAMES)} {random.choice(LAST_NAMES)}"

def random_phone():
    prefix = random.choice(["98","99","97","96","95","94","93","92",
                            "91","90","89","88","87","86","85","84",
                            "83","82","81","80","79","78","77","76",
                            "75","74","73","72","71","70","63","62"])
    return f"{prefix}{random.randint(10000000, 99999999)}"

def random_email(name):
    first = name.split()[0].lower()
    last = name.split()[1].lower()
    num = random.randint(1, 999)
    domain = random.choice(["gmail.com","yahoo.com","outlook.com",
                            "hotmail.com","rediffmail.com"])
    return f"{first}.{last}{num}@{domain}"

def random_ifsc(bank_code):
    city = random.randint(1, 9999)
    return f"{bank_code}0{city:04d}"

def random_account_no():
    return f"{random.randint(100000000000, 999999999999)}"

def random_upi(name):
    first = name.split()[0].lower()
    last = name.split()[1].lower()
    num = random.randint(1, 99)
    handle = random.choice(UPI_HANDLES)
    return f"{first}{last}{num}{handle}"

def random_date(start_year=2023, end_year=2025):
    start = datetime(start_year, 1, 1)
    end = datetime(end_year, 6, 30)
    delta = end - start
    random_days = random.randint(0, delta.days)
    random_seconds = random.randint(0, 86399)
    return start + timedelta(days=random_days, seconds=random_seconds)

def random_amount():
    # Realistic UPI amounts: mostly small, some large
    r = random.random()
    if r < 0.40:
        return round(random.uniform(10, 200), 2)      # 40% small
    elif r < 0.70:
        return round(random.uniform(200, 1000), 2)     # 30% medium
    elif r < 0.90:
        return round(random.uniform(1000, 5000), 2)    # 20% large
    elif r < 0.97:
        return round(random.uniform(5000, 20000), 2)   # 7% very large
    else:
        return round(random.uniform(20000, 100000), 2) # 3% huge

# ============================================
# GENERATE DATA
# ============================================
print("Generating data...")

users = []
bank_accounts = []
upi_ids = []
beneficiaries = []
transactions = []

used_phones = set()
used_emails = set()
used_upis = set()
used_acc_nos = set()

# --- USERS ---
for i in range(1, NUM_USERS + 1):
    name = random_name()
    while True:
        phone = random_phone()
        if phone not in used_phones:
            used_phones.add(phone)
            break
    while True:
        email = random_email(name)
        if email not in used_emails:
            used_emails.add(email)
            break

    users.append({
        "id": i,
        "name": name,
        "email": email,
        "phone": phone,
        "created": random_date(2022, 2023)
    })

# --- BANK ACCOUNTS (1-2 per user) ---
acc_id = 1
for u in users:
    num_accounts = random.choices([1, 2], weights=[75, 25])[0]
    for j in range(num_accounts):
        bank_name, bank_code = random.choice(BANKS)
        while True:
            acc_no = random_account_no()
            if acc_no not in used_acc_nos:
                used_acc_nos.add(acc_no)
                break
        balance = round(random.uniform(500, 200000), 2)
        acc_type = random.choice(["Savings", "Savings", "Savings", "Current"])

        bank_accounts.append({
            "id": acc_id,
            "user_id": u["id"],
            "bank_name": bank_name,
            "acc_no": acc_no,
            "ifsc": random_ifsc(bank_code),
            "balance": balance,
            "type": acc_type,
            "is_primary": (j == 0)
        })
        acc_id += 1

# --- UPI IDS (1 per user, linked to primary account) ---
for u in users:
    while True:
        upi = random_upi(u["name"])
        if upi not in used_upis:
            used_upis.add(upi)
            break
    primary_acc = [a for a in bank_accounts
                   if a["user_id"] == u["id"] and a["is_primary"]][0]

    upi_ids.append({
        "id": u["id"],
        "user_id": u["id"],
        "account_id": primary_acc["id"],
        "upi": upi
    })

# --- BENEFICIARIES (2-5 per user) ---
ben_id = 1
for u in users:
    num_ben = random.randint(1, 5)
    possible = [up for up in upi_ids if up["user_id"] != u["id"]]
    chosen = random.sample(possible, min(num_ben, len(possible)))
    for b in chosen:
        b_user = [x for x in users if x["id"] == b["user_id"]][0]
        beneficiaries.append({
            "id": ben_id,
            "user_id": u["id"],
            "name": b_user["name"].split()[0],
            "upi": b["upi"]
        })
        ben_id += 1

# --- TRANSACTIONS (10,000) ---
ref_counter = 1
for i in range(NUM_TRANSACTIONS):
    sender = random.choice(upi_ids)
    receiver = random.choice(upi_ids)
    while receiver["id"] == sender["id"]:
        receiver = random.choice(upi_ids)

    sender_acc = [a for a in bank_accounts
                  if a["user_id"] == sender["user_id"] and a["is_primary"]][0]
    receiver_acc = [a for a in bank_accounts
                    if a["user_id"] == receiver["user_id"] and a["is_primary"]][0]

    amount = random_amount()
    status = random.choices(
        ["SUCCESS", "FAILED", "PENDING"],
        weights=[88, 10, 2]
    )[0]
    txn_type = random.choices(
        ["PAY", "REQUEST", "REFUND"],
        weights=[90, 7, 3]
    )[0]
    remark = random.choice(TXN_REMARKS)
    ts = random_date(2023, 2025)
    ref_id = f"TXN{ts.strftime('%Y%m%d')}{ref_counter:06d}"
    ref_counter += 1

    transactions.append({
        "sender_upi": sender["id"],
        "receiver_upi": receiver["id"],
        "sender_acc": sender_acc["id"],
        "receiver_acc": receiver_acc["id"],
        "amount": amount,
        "type": txn_type,
        "status": status,
        "ref": ref_id,
        "remark": remark,
        "ts": ts.strftime("%Y-%m-%d %H:%M:%S")
    })

# Sort transactions by timestamp
transactions.sort(key=lambda x: x["ts"])

# ============================================
# WRITE SQL FILE
# ============================================
print(f"Writing {OUTPUT_FILE}...")

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write("-- ============================================\n")
    f.write(f"-- AUTO-GENERATED SEED DATA\n")
    f.write(f"-- Users: {NUM_USERS} | Transactions: {NUM_TRANSACTIONS}\n")
    f.write(f"-- Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    f.write("-- ============================================\n\n")
    f.write("USE upi_db;\n\n")

    # Disable FK checks for fast insert
    f.write("SET FOREIGN_KEY_CHECKS = 0;\n\n")

    # --- USERS ---
    f.write("-- USERS\n")
    f.write("INSERT INTO users (user_id, full_name, email, phone, password_hash, created_at, is_active) VALUES\n")
    for i, u in enumerate(users):
        comma = "," if i < len(users) - 1 else ";"
        f.write(f"({u['id']}, '{u['name']}', '{u['email']}', "
                f"'{u['phone']}', 'pbkdf2:sha256:600000$seed$hash', "
                f"'{u['created'].strftime('%Y-%m-%d %H:%M:%S')}', TRUE){comma}\n")
    f.write("\n")

    # --- BANK ACCOUNTS ---
    f.write("-- BANK ACCOUNTS\n")
    f.write("INSERT INTO bank_accounts (account_id, user_id, bank_name, account_no, ifsc_code, balance, account_type) VALUES\n")
    for i, a in enumerate(bank_accounts):
        comma = "," if i < len(bank_accounts) - 1 else ";"
        f.write(f"({a['id']}, {a['user_id']}, '{a['bank_name']}', "
                f"'{a['acc_no']}', '{a['ifsc']}', {a['balance']}, "
                f"'{a['type']}'){comma}\n")
    f.write("\n")

    # --- UPI IDS ---
    f.write("-- UPI IDS\n")
    f.write("INSERT INTO upi_ids (upi_id_pk, user_id, account_id, upi_address, upi_pin_hash, is_primary) VALUES\n")
    for i, u in enumerate(upi_ids):
        comma = "," if i < len(upi_ids) - 1 else ";"
        f.write(f"({u['id']}, {u['user_id']}, {u['account_id']}, "
                f"'{u['upi']}', 'pbkdf2:sha256:600000$seed$pinhash', TRUE){comma}\n")
    f.write("\n")

    # --- BENEFICIARIES ---
    f.write("-- BENEFICIARIES\n")
    f.write("INSERT INTO beneficiaries (ben_id, user_id, ben_name, ben_upi) VALUES\n")
    for i, b in enumerate(beneficiaries):
        comma = "," if i < len(beneficiaries) - 1 else ";"
        f.write(f"({b['id']}, {b['user_id']}, '{b['name']}', "
                f"'{b['upi']}'){comma}\n")
    f.write("\n")

    # --- TRANSACTIONS (batch of 500 per INSERT for speed) ---
    f.write("-- TRANSACTIONS\n")
    batch_size = 500
    for start in range(0, len(transactions), batch_size):
        batch = transactions[start:start + batch_size]
        f.write("INSERT INTO transactions (sender_upi, receiver_upi, sender_acc, "
                "receiver_acc, amount, txn_type, status, reference_id, remarks, timestamp) VALUES\n")
        for i, t in enumerate(batch):
            comma = "," if i < len(batch) - 1 else ";"
            remark_escaped = t['remark'].replace("'", "\\'")
            f.write(f"({t['sender_upi']}, {t['receiver_upi']}, {t['sender_acc']}, "
                    f"{t['receiver_acc']}, {t['amount']}, '{t['type']}', "
                    f"'{t['status']}', '{t['ref']}', '{remark_escaped}', "
                    f"'{t['ts']}'){comma}\n")
        f.write("\n")

    # Re-enable FK checks
    f.write("SET FOREIGN_KEY_CHECKS = 1;\n")

print(f"\n✅ Done! File: {OUTPUT_FILE}")
print(f"   Users:        {len(users)}")
print(f"   Bank Accts:   {len(bank_accounts)}")
print(f"   UPI IDs:      {len(upi_ids)}")
print(f"   Beneficiaries:{len(beneficiaries)}")
print(f"   Transactions: {len(transactions)}")
print(f"\n📌 Run in MySQL: source {OUTPUT_FILE}")