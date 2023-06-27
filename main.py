import streamlit as st


st.set_page_config(
        page_title="Brotax",
        page_icon="chart_with_upwards_trend",
        layout="wide",
    )



#ui
st.title('Income tax calculator')


#inputs
age=st.radio('Age category', ['below 60','60 or above','80 or above'], horizontal=True)

#income
income=st.number_input('income')

#Deduction
DA=st.number_input('DA')

#HRA exemption
HRA=st.number_input('HRA')

metro=st.checkbox('Do you live in metro city')

#calculation new tax
def calculate_new_tax(income, HRA, age, DA, metro):
  """Calculates the new tax for India, given the income, HRA, age, DA, and metro.

  Args:
    income: The annual income.
    HRA: The house rent allowance.
    age: The age of the taxpayer.
    DA: The deduction amount.
    metro: Whether the taxpayer lives in a metro city.

  Returns:
    The new tax amount.
  """

  # Initialize the tax slabs.
  tax_slabs = [
      (250000, 0),
      (500000, 0.05),
      (750000, 0.10 + 12500),
      (1000000, 0.15 + 37500),
      (1250000, 0.20 + 75000),
      (1500000, 0.25 + 125000),
  ]

  # Calculate the taxable income.
  taxable_income = income - HRA - DA

  # Calculate the new tax.
  new_tax = 0
  for slab_start, slab_rate in tax_slabs:
    if taxable_income <= slab_start:
      new_tax = taxable_income * slab_rate
      break

  # Add surcharge if the taxpayer lives in a metro city.
  if metro:
    new_tax += 0.02 * new_tax

  return new_tax
  

#compute
new_tax=calculate_new_tax(income, HRA, age, DA, metro)

# Display results
# st.write("Total tax old regime:", old_tax)
st.write("Total tax new regime:", new_tax)

#docs
st.header('What is Income Tax Calculator')
st.markdown('''
An Income-tax calculator is an online tool that helps to evaluate taxes based on a person’s income once the Union Budget for the year is announced. Individuals falling under the taxable income bracket are liable to pay a specific portion of their net annual income as tax. Income tax can be paid either as tax deducted at source while disbursement of monthly salary, or through the income tax returns portal managed by the Central Board of Direct Taxes (CBDT). The provision for online payment of taxes is to ensure individuals pay their stipulated dues on any earnings generated from other sources.The IT calculator given on this page is aligned with the updates announced in the Union Budget for FY 2023-24 and AY 2024-25.''')

st.header('About us')
st.markdown('''This income tax calculator project was created by Hiten and Devesh, two students in XII-'A' at KV No.1 Manglore Panambur. The project was guided by Sunil sir, a computer science teacher at the school.''')

st.header('The Goal')
st.markdown('''The goal of the project was to create a simple and easy-to-use income tax calculator that could be used by anyone. The calculator takes into account the latest Indian income tax slabs and deductions, and it provides a clear and concise output.''')

st.header('Tech used')
st.markdown('''Pythom 3.7 \nStreamlit \nMySQL''')





