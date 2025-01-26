# calculations.py
import sqlite3

def init_database(db_name="bridge_costs.db"):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cost_data (
            Material TEXT,
            BaseRate REAL,
            MaintenanceRate REAL,
            RepairRate REAL,
            DemolitionRate REAL,
            EnvironmentalFactor REAL,
            SocialFactor REAL,
            DelayFactor REAL
        )
    """)

    cursor.execute("SELECT COUNT(*) FROM cost_data")
    if cursor.fetchone()[0] == 0:
        cursor.executemany("""
            INSERT INTO cost_data VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, [
            ("Steel", 3000, 50, 200, 100, 10, 0.5, 0.3),
            ("Concrete", 2500, 75, 150, 80, 8, 0.6, 0.2)
        ])
        conn.commit()

    return conn, cursor


def calculate_costs(cursor, span_length, width, traffic_volume, design_life):
    cursor.execute("SELECT * FROM cost_data")
    cost_data = cursor.fetchall()

    results = []
    for material, base_rate, maintenance_rate, repair_rate, demolition_rate, env_factor, social_factor, delay_factor in cost_data:
        construction_cost = span_length * width * base_rate
        maintenance_cost = span_length * width * maintenance_rate * design_life
        repair_cost = span_length * width * repair_rate
        demolition_cost = span_length * width * demolition_rate
        environmental_cost = span_length * width * env_factor
        social_cost = traffic_volume * social_factor * design_life
        user_cost = traffic_volume * delay_factor * design_life
        total_cost = (construction_cost + maintenance_cost + repair_cost +
                      demolition_cost + environmental_cost + social_cost + user_cost)

        results.append([material, construction_cost, maintenance_cost, repair_cost, demolition_cost,
                        environmental_cost, social_cost, user_cost, total_cost])

    return results
