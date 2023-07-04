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
DA=st.number_input('Deduction')

#HRA exemption
HRA=st.number_input('HRA')

metro=st.checkbox('Do you live in metro city')

#calculation new tax

def newtaxcalc(age, income):
  """Calculates income tax for the new tax regime.

  Args:
    age: The age of the taxpayer.
    income: The income of the taxpayer.

  Returns:
    total tax
  """
  tax = 0
  income -= 50000

  if income <= 300000:
    tax = 0
  elif income <= 600000:
    tax = (income - 300000) * 0.05
  elif income <= 900000:
    tax = 15000 + (income - 600000) * 0.1
  elif income <= 1200000:
    tax = 45000 + (income - 900000) * 0.15
  elif income <= 1500000:
    tax = 90000 + (income - 1200000) * 0.20
  else:
    tax = 150000 + (income - 1500000) * 0.3

  section = []
  if income <= 700000:
    tax -= 25000
    section.append('87A')

  if tax < 0:
    tax = 0

  cess = tax * 0.04
  ttax = tax + cess

  return ttax

#calculation of old tax 
def oldtaxcalc():
    pass

#compute
new_tax=newtaxcalc(age,income)

# Display results
# st.write("Total tax old regime:₹", old_tax)
st.write("Total tax new regime:₹",new_tax)

st.divider()

#docs
st.header('What is Income Tax Calculator')
st.markdown('''
An Income-tax calculator is an online tool that helps to evaluate taxes based on a person’s income once the Union Budget for the year is announced. Individuals falling under the taxable income bracket are liable to pay a specific portion of their net annual income as tax. Income tax can be paid either as tax deducted at source while disbursement of monthly salary, or through the income tax returns portal managed by the Central Board of Direct Taxes (CBDT). The provision for online payment of taxes is to ensure individuals pay their stipulated dues on any earnings generated from other sources.The IT calculator given on this page is aligned with the updates announced in the Union Budget for FY 2023-24 and AY 2024-25.''')

st.divider()

st.subheader('About us')
st.markdown('''This income tax calculator project was created by Hiten and Devesh, two students in XII-'A' at KV No.1 Manglore Panambur. The project was guided by Sunil sir, computer science teacher at the school.''')

st.subheader('The Goal')
st.markdown('''The goal of the project was to create a simple and easy-to-use income tax calculator that could be used by anyone. The calculator takes into account the latest Indian income tax slabs and deductions, and it provides a clear and concise output.''')

st.subheader('Tech used')
st.markdown('''Pythom 3.7 \nStreamlit \nMySQL''')





