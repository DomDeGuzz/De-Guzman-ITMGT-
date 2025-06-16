def savings(gross_pay, tax_rate, expenses):
    after_tax_pay = int(gross_pay * (1 - tax_rate))
    remaining = after_tax_pay - expenses
    return remaining

def material_waste(total_material, material_units, num_jobs, job_consumption):
    total_consumed = num_jobs * job_consumption
    waste = total_material - total_consumed
    return f"{waste}{material_units}"

def interest(principal, rate, periods):
    final_value = principal + int(principal * rate * periods)
    return final_value

