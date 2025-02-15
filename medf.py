import streamlit as st
import mysql.connector
from mysql.connector import Error

# MySQL connection details
def create_connection():
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',        
            database='test',    
            user='root',             
            password='Lemonade'      
        )
        if connection.is_connected():
            return connection
    except Error as e:
        st.error(f"Error connecting to MySQL: {e}")
        return None


# Function to insert data into the database
def insert_data(connection, f_name,l_name,dob,gender,nationality,
                street_address,atoll,island,postal_code,
                disability,disability_status,
                me_email,me_tphone,
                lf_status,isic_section,isic_division,
                job_role,contract_type,contract_expiry,
                weekly_hrs,salorwage,
                bus_name,bus_atoll,bus_island,bus_email,bus_tphone,
                visa_status,visa_expiry):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users (f_name,l_name,dob,gender,nationality,street_address,atoll,island,postal_code,disability,disability_status,me_email,me_tphone,lf_status,isic_section,isic_division,job_role,contract_type,contract_expiry,weekly_hrs,salorwage,bus_name,bus_atoll,bus_island,bus_email,bus_tphone,visa_status,visa_expiry) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", 
                (f_name,l_name,dob,gender,nationality,
                street_address,atoll,island,postal_code,
                disability,disability_status,
                me_email,me_tphone,
                lf_status,isic_section,isic_division,
                job_role,contract_type,contract_expiry,
                weekly_hrs,salorwage,
                bus_name,bus_atoll,bus_island,bus_email,bus_tphone,
                visa_status,visa_expiry))
    connection.commit()

# Streamlit form to collect user input
def form():
    st.title('Streamlit Form with MySQL')

    # Creating a form to collect data
    with st.form(key='user_form'):
        f_name = st.text_input("Enter your first name")
        l_name= st.text_input("Enter your last name")
        dob = st.date_input("Enter your date of birth")
        gender = st.selectbox("Gender",("Male", "Female"))
        nationality = st.selectbox("What is your nationality?",
             ("Afghanistan", "Albania", "Algeria", "Andorra", "Angola", 
              "Antigua and Barbuda", "Argentina", "Armenia", "Australia", 
              "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", 
              "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bhutan", 
              "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", 
              "Brunei", "Bulgaria", "Burkina Faso", "Burundi", "Cabo Verde", 
              "Cambodia", "Cameroon", "Canada", "Central African Republic", 
              "Chad", "Chile", "China", "Colombia", "Comoros", "Costa Rica", 
              "Croatia", "Cuba", "Cyprus", "Czech Republic", "Denmark", 
              "Djibouti", "Dominica", "Dominican Republic", "East Timor", "Ecuador", 
              "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", 
              "Eswatini", "Ethiopia", "Fiji", "Finland", "France", "Gabon", 
              "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Grenada", 
              "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", 
              "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", 
              "Iraq", "Ireland", "Israel", "Italy", "Ivory Coast", "Jamaica", 
              "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Kuwait", 
              "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", 
              "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar", 
              "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", 
              "Mauritania", "Mauritius", "Mexico", "Micronesia", "Moldova", "Monaco", 
              "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar", "Namibia", 
              "Nauru", "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Niger", 
              "Nigeria", "North Korea", "North Macedonia", "Norway", "Oman", "Pakistan", 
              "Palau", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", 
              "Poland", "Portugal", "Qatar", "Romania", "Russia", "Rwanda", 
              "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", 
              "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal", 
              "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", 
              "Solomon Islands", "Somalia", "South Africa", "South Korea", "Spain", "Sri Lanka", 
              "Sudan", "Suriname", "Sweden", "Switzerland", "Syria", "Taiwan", "Tajikistan", 
              "Tanzania", "Thailand", "Togo", "Tonga", "Trinidad and Tobago", "Tunisia", 
              "Turkey", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", 
              "United Kingdom", "United States", "Uruguay", "Uzbekistan", "Vanuatu", "Vatican City", 
              "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe"))
        street_address = st.text_input("Street Address")
        atoll = st.selectbox("Atoll",("Haa Alifu", "Haa Dhaalu", "Shaviyani", "Noonu", "Raa", "Baa", 
              "Lhaviyani", "Kaafu", "Alif Alif", "Alif Dhaalu", "Vaavu", "Meemu", "Faafu", "Dhaalu", 
              "Thaa", "Laamu", "Gaafu Alif", "Gaafu Dhaalu", "Gnaviyani", "Seenu"))
        island = st.selectbox("Island",("AA.Bodufolhudhoo", "AA.Feridhoo", "AA.Himandhoo", "AA.Maalhos", "AA.Mathiveri", 
        "AA.Rasdhoo", "AA.Thoddoo", "AA.Ukulhas", "Adh.Dhagethi", "Adh.Dhidhdhoo", "Adh.Dhigurah", "Adh.Fenfushi", 
        "Adh.Hangnameedhoo", "Adh.Kuburudhoo", "Adh.Maamigili", "Adh.Mahibadhoo", "Adh.Mandhoo", "Adh.Omadhoo", 
        "B.Dharavandhoo", "B.Dhonfanu", "B.Eydhafushi", "B.Fehendhoo", "B.Fulhadhoo", "B.Goidhoo", "B.Hithaadhoo", 
        "B.Kamadhoo", "B.Kendhoo", "B.Kihaadhoo", "B.Kudarikilu", "B.Maalhos", "B.Thulhaadhoo", "Dh.Badidhoo", 
        "Dh.Hulhudheli", "Dh.Kudahuvadhoo", "Dh.Maaeboodhoo", "Dh.Meedhoo", "Dh.Ribudhoo", "F.Biledhdhoo", "F.Dharaboodhoo", 
        "F.Feeali", "F.Magoodhoo", "F.Nilandhoo", "GA.Dhaandhoo", "GA.Dhevvadhoo", "GA.Gemanafushi", "GA.Kanduhulhudhoo", 
        "GA.Kodey", "GA.Kolamaafushi", "GA.Maamendhoo", "GA.Nilandhoo", "GA.Viligili", "GDh.Fares-Maathodaa", "GDh.Fiyoari", 
        "GDh.Gadhdhoo", "GDh.Hoadedhdhoo", "GDh.Madeveli", "GDh.Nadallaa", "GDh.Rathafandhoo", "GDh.Thinadhoo", "GDh.Vaadhoo", 
        "Gn.Fuvahmulah", "HA.Baarah", "HA.Dhidhdhoo", "HA.Filladhoo", "HA.Hoarafushi", "HA.Ihavandhoo", "HA.Kelaa", "HA.Maarandhoo", "HA.Mulhadhoo", 
        "HA.Muraidhoo", "HA.Thakandhoo", "HA.Thuraakunu", "HA.Uligamu", "HA.Utheemu", "HA.Vashafaru", "HDh.Finey", "HDh.Hanimaadhoo", 
        "HDh.Hirimaradhoo", "HDh.Kulhudhuffushi", "HDh.Kumundhoo", "HDh.Kuribi", "HDh.Makunudhoo", "HDh.Naivaadhoo", "HDh.Nellaidhoo", 
        "HDh.Neykurendhoo", "HDh.Nolhivaramu", "HDh.Nolhivaranfaru", "HDh.Vaikaradhoo", "K.Dhiffushi", "K.Gaafaru", "K.Gulhi", 
        "K.Guraidhoo", "K.Himmafushi", "K.Huraa", "K.Kaashidhoo", "K.Maafushi", "K.Thulusdhoo", "L.Dhabidhoo", "L.Fonadhoo", 
        "L.Gamu", "L.Hithadhoo", "L.Isdhoo", "L.Kalaidhoo", "L.Kunahandhoo", "L.Maabaidhoo", "L.Maamendhoo", "L.Maavah", 
        "L.Mundhoo", "Lh.Hinnavaru", "Lh.Kurendhoo", "Lh.Naifaru", "Lh.Olhuvelifushi", "M.Dhiggaru", "M.Kolhufushi", 
        "M.Maduvvari", "M.Mulah", "M.Muli", "M.Naalaafushi", "M.Raimandhoo", "M.Veyvah", "Hulhumaale", 
        "K.Hulhule", "Vilimale", "Male", "N.Fodhdhoo", "N.Henbadhoo", "N.Holhudhoo", 
        "N.Kedhikulhudhoo", "N.Kudafari", "N.Landhoo", "N.Lhohi", "N.Maafaru", "N.Maalhendhoo", "N.Magoodhoo", 
        "N.Manadhoo", "N.Miladhoo", "N.Velidhoo", "R.Agolhitheemu", "R.Alifushi", "R.Dhuvaafaru", "R.Fainu", 
        "R.Hulhudhuffaaru", "R.Iguraidhoo", "R.Innamaadhoo", "R.Kinolhas", "R.Maakurathu", "R.Maduvvari", "R.Meedhoo", 
        "R.Rasgetheemu", "R.Rasmaadhoo", "R.Ugoofaaru", "R.Vaadhoo", "S.Feydhoo", "S.Hithadhoo", "S.Hulhudhoo", "S.Maradhoo", 
        "S.Maradhoo-Feydhoo", "S.Meedhoo", "Sh.Bilehffahi", "Sh.Feevah", "Sh.Feydhoo", "Sh.Foakaidhoo", "Sh.Funadhoo", "Sh.Goidhoo", 
        "Sh.Kaditheemu", "Sh.Komandoo", "Sh.Lhaimagu", "Sh.Maaugoodhoo", "Sh.Maroshi", "Sh.Milandhoo", "Sh.Narudhoo", "Sh.Noomaraa", 
        "Th.Buruni", "Th.Dhiyamigili", "Th.Gaadhiffushi", "Th.Guraidhoo", "Th.Hirilandhoo", "Th.Kadoodhoo", "Th.Kibidhoo", 
        "Th.Madifushi", "Th.Omadhoo", "Th.Thimarafushi", "Th.Vandhoo", "Th.Veymandoo", "Th.Vilufushi", "V.Felidhoo", "V.Fulidhoo", 
        "V.Keyodhoo", "V.Rakeedhoo", "V.Thinadhoo"))
        postal_code = st.number_input("Postal Code",step=1)
        disability=st.selectbox("Disability Status",("with disability","without disability"))
        disability_status=st.selectbox("Disability severity",("Not applicable","Mild","Moderate","Severe"))
        me_email=st.text_input("Personal email address")
        me_tphone=st.number_input("Personal mobile number",step=1)

        lf_status=st.radio("Labor Force Status",["Employed", "Unemployed","Outside Labor Force"])
        isic_section=st.selectbox("Employment (ISIC) section",["Not applicable","Section A: Agriculture, Forestry, and Fishing", 
                "Section B: Mining and Quarrying", "Section C: Manufacturing", "Section D: Electricity, Gas, Steam, and Air Conditioning Supply", 
                "Section E: Water Supply; Sewerage, Waste Management, and Remediation Activities", "Section F: Construction", 
                "Section G: Wholesale and Retail Trade; Repair of Motor Vehicles and Motorcycles", "Section H: Transportation and Storage", 
                "Section I: Accommodation and Food Service Activities", "Section J: Information and Communication", 
                "Section K: Financial and Insurance Activities", "Section L: Real Estate Activities", 
                "Section M: Professional, Scientific, and Technical Activities", "Section N: Administrative and Support Service Activities", 
                "Section O: Public Administration and Defence; Compulsory Social Security", "Section P: Education", 
                "Section Q: Human Health and Social Work Activities", "Section R: Arts, Entertainment, and Recreation", 
                "Section S: Other Service Activities", 
                "Section T: Activities of Households as Employers; Undifferentiated Goods- and Services-Producing Activities of Households for Own Use", 
                "Section U: Activities of Extraterritorial Organizations and Bodies","Unable to codify"])
        isic_division=st.selectbox("Employment Division",["Not applicable","A01: Crop and animal production, hunting, and related service activities", "A02: Forestry and logging", 
                                                          "A03: Fishing and aquaculture", "B05: Mining of coal and lignite", "B06: Extraction of crude petroleum and natural gas", 
                                                          "B07: Mining of metal ores", "B08: Other mining and quarrying", "B09: Mining support service activities", 
                                                          "C10: Manufacture of food products", "C11: Manufacture of beverages", "C12: Manufacture of tobacco products", 
                                                          "C13: Manufacture of textiles", "C14: Manufacture of wearing apparel", "C15: Manufacture of leather and related products", 
                                                          "C16: Manufacture of wood and of products of wood and cork, except furniture", "C17: Manufacture of paper and paper products", 
                                                          "C18: Printing and reproduction of recorded media", "C19: Manufacture of coke and refined petroleum products", 
                                                          "C20: Manufacture of chemicals and chemical products", "C21: Manufacture of pharmaceuticals, medicinal chemical, and botanical products", 
                                                          "C22: Manufacture of rubber and plastics products", "C23: Manufacture of other non-metallic mineral products", "C24: Manufacture of basic metals", 
                                                          "C25: Manufacture of fabricated metal products, except machinery and equipment", "C26: Manufacture of computer, electronic, and optical products", 
                                                          "C27: Manufacture of electrical equipment", "C28: Manufacture of machinery and equipment n.e.c.", "C29: Manufacture of motor vehicles, trailers, and semitrailers", 
                                                          "C30: Manufacture of other transport equipment", "C31: Manufacture of furniture", "C32: Other manufacturing", "C33: Repair and installation of machinery and equipment", 
                                                          "D35: Electricity, gas, steam, and air conditioning supply", "E36: Water collection, treatment, and supply", "E37: Sewerage", 
                                                          "E38: Waste collection, treatment, and disposal activities; materials recovery", "E39: Remediation activities and other waste management services", 
                                                          "F41: Construction of buildings", "F42: Civil engineering", "F43: Specialized construction activities", "G45: Wholesale and retail trade and repair of motor vehicles and motorcycles", 
                                                          "G46: Wholesale trade, except of motor vehicles and motorcycles", "G47: Retail trade, except of motor vehicles and motorcycles", 
                                                          "H49: Land transport and transport via pipelines", "H50: Water transport", "H51: Air transport", "H52: Warehousing and support activities for transportation", 
                                                          "H53: Postal and courier activities", "I55: Accommodation", "I56: Food and beverage service activities", "J58: Publishing activities", 
                                                          "J59: Motion picture, video, and television program production, sound recording, and music publishing activities", "J60: Programming and broadcasting activities", 
                                                          "J61: Telecommunications", "J62: Computer programming, consultancy, and related activities", "J63: Information service activities", 
                                                          "K64: Financial service activities, except insurance and pension funding", "K65: Insurance, reinsurance, and pension funding, except compulsory social security", 
                                                          "K66: Activities auxiliary to financial services and insurance activities", "L68: Real estate activities", "M69: Legal and accounting activities", 
                                                          "M70: Activities of head offices; management consultancy activities", "M71: Architectural and engineering activities; technical testing and analysis", 
                                                          "M72: Scientific research and development", "M73: Advertising and market research", "M74: Other professional, scientific, and technical activities", 
                                                          "M75: Veterinary activities", "N77: Rental and leasing activities", "N78: Employment activities", "N79: Travel agency, tour operator, and other reservation service and related activities", 
                                                          "N80: Security and investigation activities", "N81: Services to buildings and landscape activities", "N82: Office administrative, office support, and other business support activities", 
                                                          "O84: Public administration and defense; compulsory social security", "P85: Education", "Q86: Human health activities", "Q87: Residential care activities", "Q88: Social work activities without accommodation", 
                                                          "R90: Creative, arts, and entertainment activities", "R91: Libraries, archives, museums, and other cultural activities", "R92: Gambling and betting activities", 
                                                          "R93: Sports activities and amusement and recreation activities", "S94: Activities of membership organizations", "S95: Repair of computers and personal and household goods", 
                                                          "S96: Other personal service activities", "T97: Activities of households as employers of domestic personnel", "T98: Undifferentiated goods- and services-producing activities of private households for own use", 
                                                          "U99: Activities of extraterritorial organizations and bodies"])
        job_role=st.selectbox("Job Role",["Not applicable","Employee","Group worker","Own account worker","Employer / Owner (with hired employees)",
                                "Helper (without pay) in a family business","Not stated","Paid apprentice or intern","Own account worker (with family members)","Not applicable"])
        contract_type=st.radio("Contract type",["Not applicable","Full-time","Part-time","Fixed-term"])
        contract_expiry=st.date_input("Enter the date of contract expiry")
        weekly_hrs=st.slider("Weekly Hours",min_value=0,max_value=168,step=1)
        salorwage = st.slider('Monthly income', min_value=5000, max_value=200000, step=5000)

        bus_name=st.text_input("Business Name")
        bus_atoll = st.selectbox("Business Atoll",("Not applicable","Haa Alifu", "Haa Dhaalu", "Shaviyani", "Noonu", "Raa", "Baa", 
              "Lhaviyani", "Kaafu", "Alif Alif", "Alif Dhaalu", "Vaavu", "Meemu", "Faafu", "Dhaalu", 
              "Thaa", "Laamu", "Gaafu Alif", "Gaafu Dhaalu", "Gnaviyani", "Seenu"))
        bus_island = st.selectbox("Business Island",("Not applicable","AA.Bodufolhudhoo", "AA.Feridhoo", "AA.Himandhoo", "AA.Maalhos", "AA.Mathiveri", 
        "AA.Rasdhoo", "AA.Thoddoo", "AA.Ukulhas", "Adh.Dhagethi", "Adh.Dhidhdhoo", "Adh.Dhigurah", "Adh.Fenfushi", 
        "Adh.Hangnameedhoo", "Adh.Kuburudhoo", "Adh.Maamigili", "Adh.Mahibadhoo", "Adh.Mandhoo", "Adh.Omadhoo", 
        "B.Dharavandhoo", "B.Dhonfanu", "B.Eydhafushi", "B.Fehendhoo", "B.Fulhadhoo", "B.Goidhoo", "B.Hithaadhoo", 
        "B.Kamadhoo", "B.Kendhoo", "B.Kihaadhoo", "B.Kudarikilu", "B.Maalhos", "B.Thulhaadhoo", "Dh.Badidhoo", 
        "Dh.Hulhudheli", "Dh.Kudahuvadhoo", "Dh.Maaeboodhoo", "Dh.Meedhoo", "Dh.Ribudhoo", "F.Biledhdhoo", "F.Dharaboodhoo", 
        "F.Feeali", "F.Magoodhoo", "F.Nilandhoo", "GA.Dhaandhoo", "GA.Dhevvadhoo", "GA.Gemanafushi", "GA.Kanduhulhudhoo", 
        "GA.Kodey", "GA.Kolamaafushi", "GA.Maamendhoo", "GA.Nilandhoo", "GA.Viligili", "GDh.Fares-Maathodaa", "GDh.Fiyoari", 
        "GDh.Gadhdhoo", "GDh.Hoadedhdhoo", "GDh.Madeveli", "GDh.Nadallaa", "GDh.Rathafandhoo", "GDh.Thinadhoo", "GDh.Vaadhoo", 
        "Gn.Fuvahmulah", "HA.Baarah", "HA.Dhidhdhoo", "HA.Filladhoo", "HA.Hoarafushi", "HA.Ihavandhoo", "HA.Kelaa", "HA.Maarandhoo", "HA.Mulhadhoo", 
        "HA.Muraidhoo", "HA.Thakandhoo", "HA.Thuraakunu", "HA.Uligamu", "HA.Utheemu", "HA.Vashafaru", "HDh.Finey", "HDh.Hanimaadhoo", 
        "HDh.Hirimaradhoo", "HDh.Kulhudhuffushi", "HDh.Kumundhoo", "HDh.Kuribi", "HDh.Makunudhoo", "HDh.Naivaadhoo", "HDh.Nellaidhoo", 
        "HDh.Neykurendhoo", "HDh.Nolhivaramu", "HDh.Nolhivaranfaru", "HDh.Vaikaradhoo", "K.Dhiffushi", "K.Gaafaru", "K.Gulhi", 
        "K.Guraidhoo", "K.Himmafushi", "K.Huraa", "K.Kaashidhoo", "K.Maafushi", "K.Thulusdhoo", "L.Dhabidhoo", "L.Fonadhoo", 
        "L.Gamu", "L.Hithadhoo", "L.Isdhoo", "L.Kalaidhoo", "L.Kunahandhoo", "L.Maabaidhoo", "L.Maamendhoo", "L.Maavah", 
        "L.Mundhoo", "Lh.Hinnavaru", "Lh.Kurendhoo", "Lh.Naifaru", "Lh.Olhuvelifushi", "M.Dhiggaru", "M.Kolhufushi", 
        "M.Maduvvari", "M.Mulah", "M.Muli", "M.Naalaafushi", "M.Raimandhoo", "M.Veyvah", "Hulhumaale", 
        "K.Hulhule", "Vilimale", "Male", "N.Fodhdhoo", "N.Henbadhoo", "N.Holhudhoo", 
        "N.Kedhikulhudhoo", "N.Kudafari", "N.Landhoo", "N.Lhohi", "N.Maafaru", "N.Maalhendhoo", "N.Magoodhoo", 
        "N.Manadhoo", "N.Miladhoo", "N.Velidhoo", "R.Agolhitheemu", "R.Alifushi", "R.Dhuvaafaru", "R.Fainu", 
        "R.Hulhudhuffaaru", "R.Iguraidhoo", "R.Innamaadhoo", "R.Kinolhas", "R.Maakurathu", "R.Maduvvari", "R.Meedhoo", 
        "R.Rasgetheemu", "R.Rasmaadhoo", "R.Ugoofaaru", "R.Vaadhoo", "S.Feydhoo", "S.Hithadhoo", "S.Hulhudhoo", "S.Maradhoo", 
        "S.Maradhoo-Feydhoo", "S.Meedhoo", "Sh.Bilehffahi", "Sh.Feevah", "Sh.Feydhoo", "Sh.Foakaidhoo", "Sh.Funadhoo", "Sh.Goidhoo", 
        "Sh.Kaditheemu", "Sh.Komandoo", "Sh.Lhaimagu", "Sh.Maaugoodhoo", "Sh.Maroshi", "Sh.Milandhoo", "Sh.Narudhoo", "Sh.Noomaraa", 
        "Th.Buruni", "Th.Dhiyamigili", "Th.Gaadhiffushi", "Th.Guraidhoo", "Th.Hirilandhoo", "Th.Kadoodhoo", "Th.Kibidhoo", 
        "Th.Madifushi", "Th.Omadhoo", "Th.Thimarafushi", "Th.Vandhoo", "Th.Veymandoo", "Th.Vilufushi", "V.Felidhoo", "V.Fulidhoo", 
        "V.Keyodhoo", "V.Rakeedhoo", "V.Thinadhoo"))
        bus_email=st.text_input("Business Email")
        bus_tphone=st.number_input("Business Telephone Number",step=1)

        visa_status=st.radio("Select your VISA status",["Issued", "In progress","Rejected"])
        visa_expiry = st.date_input("State date of expiry of VISA")


        # Submit button
        submit_button = st.form_submit_button(label='Submit')

    # On form submission
    if submit_button:
        # Get the database connection
        connection = create_connection()
        if connection:
            # Insert data into the database
            insert_data(connection,f_name,l_name,dob,gender,nationality,
                street_address,atoll,island,postal_code,
                disability,disability_status,
                me_email,me_tphone,
                lf_status,isic_section,isic_division,
                job_role,contract_type,contract_expiry,
                weekly_hrs,salorwage,
                bus_name,bus_atoll,bus_island,bus_email,bus_tphone,
                visa_status,visa_expiry)
            st.success(f'Data for {f_name} has been saved successfully!')
            connection.close()  # Close the connection

# Initialize the app
if __name__ == "__main__":
    # Create MySQL connection and table
    connection = create_connection()
    if connection:
        connection.close()  # Close the connection

    # Display the form
    form()
