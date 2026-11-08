
import streamlit as st
import html
import textwrap

# ==========================================
# 1. PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Student Grade Manager",
    page_icon="🎓",
    layout="wide"
)


# ==========================================
# 2. HTML RENDERING FUNCTION
# ==========================================

def render_html(content):
    st.html(textwrap.dedent(content).strip())


# ==========================================
# 3. CUSTOM CSS
# ==========================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

.stApp {
    background: #F4F7FC;
    font-family: 'Inter', sans-serif;
}

.block-container {
    max-width: 1200px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

#MainMenu, footer {
    visibility: hidden;
}

[data-testid="stHeader"] {
    background: transparent;
}


/* ==========================================
   HERO SECTION
========================================== */

.hero {
    background: linear-gradient(120deg, #142B52, #2455A4);
    padding: 35px 38px;
    border-radius: 20px;
    margin-bottom: 28px;
    color: white;
    box-shadow: 0 12px 30px rgba(30,65,120,0.15);
}

.hero-tag {
    display: inline-block;
    background: rgba(255,255,255,0.15);
    padding: 7px 13px;
    border-radius: 30px;
    font-size: 12px;
    font-weight: 600;
    margin-bottom: 14px;
}

.hero h1 {
    color: white !important;
    font-size: 32px;
    font-weight: 800;
    margin: 0 0 10px;
}

.hero p {
    color: #DCE8FF;
    font-size: 14px;
    margin: 0;
}


/* ==========================================
   SECTION HEADINGS
========================================== */

.section-title {
    font-size: 19px;
    font-weight: 700;
    color: #172B4D;
    margin-bottom: 5px;
}

.section-subtitle {
    font-size: 13px;
    color: #77849A;
    margin-bottom: 18px;
}


/* ==========================================
   STUDENT FORM
========================================== */

div[data-testid="stForm"] {
    background: white;
    padding: 24px;
    border: 1px solid #E8EDF5;
    border-radius: 16px;
    box-shadow: 0 5px 20px rgba(30,50,90,0.05);
}


/* INPUT LABELS */

.stTextInput label,
.stNumberInput label {
    font-weight: 600 !important;
    color: #172B4D !important;
    font-size: 13px !important;
}


/* INPUT TEXT - BLACK COLOR */

.stTextInput input,
.stNumberInput input,
[data-testid="stTextInput"] input,
[data-testid="stNumberInput"] input {

    color: #000000 !important;
    -webkit-text-fill-color: #000000 !important;

    background: #FAFBFE !important;

    border: 1px solid #DCE3EF !important;
    border-radius: 9px !important;

    min-height: 43px;

    opacity: 1 !important;
    font-size: 14px !important;
    font-weight: 500 !important;
}


/* PLACEHOLDER TEXT */

.stTextInput input::placeholder,
.stNumberInput input::placeholder {

    color: #9CA3AF !important;
    -webkit-text-fill-color: #9CA3AF !important;
    opacity: 1 !important;
}


/* INPUT FOCUS */

.stTextInput input:focus,
.stNumberInput input:focus {

    border: 1px solid #2864D9 !important;
    box-shadow: 0 0 0 2px rgba(40,100,217,0.10) !important;
}


/* ==========================================
   ADD STUDENT BUTTON
========================================== */

.stFormSubmitButton button {

    background: linear-gradient(120deg, #2864D9, #174BB5);

    color: #FFFFFF !important;

    border: none;
    border-radius: 9px;

    font-weight: 600;
    min-height: 44px;

    transition: all 0.2s ease;
}

.stFormSubmitButton button:hover {

    background: #123D98;

    box-shadow: 0 5px 15px rgba(40,100,217,0.25);

    transform: translateY(-1px);
}


/* ==========================================
   PERFORMANCE METRIC CARDS
========================================== */

.metric-card {

    background: white;

    padding: 21px;

    border-radius: 15px;

    border: 1px solid #E8EDF5;

    box-shadow: 0 5px 18px rgba(30,50,90,0.05);

    min-height: 125px;
}

.metric-label {

    color: #78869C;

    font-size: 12px;

    font-weight: 600;

    margin-bottom: 12px;
}

.metric-value {

    color: #172B4D;

    font-size: 27px;

    font-weight: 800;
}

.metric-icon {

    font-size: 20px;

    margin-bottom: 9px;
}


/* ==========================================
   STUDENT COUNT
========================================== */

.student-count {

    display: inline-block;

    background: #EAF1FF;

    color: #2459BB;

    padding: 7px 13px;

    border-radius: 30px;

    font-size: 12px;

    font-weight: 700;
}


/* ==========================================
   STUDENT RESULTS TABLE
========================================== */

.table-wrap {

    background: white;

    border: 1px solid #E8EDF5;

    border-radius: 15px;

    padding: 15px;

    overflow-x: auto;

    box-shadow: 0 5px 18px rgba(30,50,90,0.04);
}

.student-table {

    width: 100%;

    border-collapse: collapse;

    font-size: 13px;
}

.student-table th {

    background: #F5F7FC;

    color: #64748B;

    padding: 15px;

    text-align: left;

    font-weight: 700;
}

.student-table td {

    padding: 16px 15px;

    color: #344563;

    border-bottom: 1px solid #EEF1F6;
}

.student-table tr:last-child td {

    border-bottom: none;
}


/* ==========================================
   GRADE BADGES
========================================== */

.grade {

    display: inline-block;

    padding: 5px 12px;

    border-radius: 20px;

    font-weight: 700;

    font-size: 12px;
}

.grade-a {
    background: #DDF7E9;
    color: #16834D;
}

.grade-b {
    background: #E0F0FF;
    color: #1765B5;
}

.grade-c {
    background: #FFF3D8;
    color: #A66A00;
}

.grade-d {
    background: #FFE8DC;
    color: #C45B24;
}

.grade-e {
    background: #FFE2E5;
    color: #C33D50;
}


/* ==========================================
   EMPTY STATE
========================================== */

.empty-state {

    background: white;

    border: 1px dashed #C9D4E5;

    border-radius: 15px;

    padding: 38px 15px;

    text-align: center;

    color: #7B879B;
}

.empty-icon {

    font-size: 36px;

    margin-bottom: 10px;
}

.empty-title {

    color: #344563;

    font-weight: 700;

    font-size: 16px;
}


/* ==========================================
   FOOTER
========================================== */

.footer {

    text-align: center;

    color: #94A0B2;

    font-size: 12px;

    padding: 25px 0 5px;
}


/* ==========================================
   RESPONSIVE DESIGN
========================================== */

@media(max-width: 768px) {

    .hero {
        padding: 25px 20px;
    }

    .hero h1 {
        font-size: 25px;
    }

    .block-container {
        padding: 1rem;
    }

    .metric-card {
        padding: 14px;
    }

    .metric-value {
        font-size: 22px;
    }

}

</style>
""", unsafe_allow_html=True)


# ==========================================
# 4. GRADE CALCULATION
# ==========================================

def get_grade(mark):

    if mark >= 90:
        return "A"

    elif mark >= 80:
        return "B"

    elif mark >= 70:
        return "C"

    elif mark >= 60:
        return "D"

    else:
        return "E"


# ==========================================
# 5. SESSION STATE
# ==========================================

if "students" not in st.session_state:

    st.session_state.students = []


# ==========================================
# 6. HERO SECTION
# ==========================================

render_html("""
<div class="hero">

    <div class="hero-tag">
        🎓 STUDENT MANAGEMENT SYSTEM
    </div>

    <h1>Student Grade Manager</h1>

    <p>
        Manage student records, track academic performance
        and monitor class results in one place.
    </p>

</div>
""")


# ==========================================
# 7. MAIN LAYOUT
# ==========================================

left_col, right_col = st.columns(
    [0.9, 1.4],
    gap="large"
)


# ==========================================
# 8. ADD NEW STUDENT
# ==========================================

with left_col:

    render_html("""
    <div class="section-title">
        Add New Student
    </div>

    <div class="section-subtitle">
        Enter student details below.
    </div>
    """)

    with st.form("student_form", clear_on_submit=True):

        name = st.text_input(
            "Student Name",
            placeholder="Enter student name"
        )

        mark = st.number_input(
            "Student Mark",
            min_value=0,
            max_value=100,
            value=0,
            step=1,
            format="%d",
            help="Enter a mark between 0 and 100."
        )

        submitted = st.form_submit_button(
            "＋  Add Student",
            use_container_width=True
        )

        if submitted:

            if not name.strip():

                st.error(
                    "Please enter the student name."
                )

            else:

                student = {
                    "Name": name.strip(),
                    "Mark": mark,
                    "Grade": get_grade(mark)
                }

                st.session_state.students.append(student)

                st.success(
                    f"{name.strip()} added successfully!"
                )


# ==========================================
# 9. PERFORMANCE OVERVIEW
# ==========================================

with right_col:

    render_html("""
    <div class="section-title">
        Performance Overview
    </div>

    <div class="section-subtitle">
        Your class performance at a glance.
    </div>
    """)

    students = st.session_state.students

    if students:

        marks = [s["Mark"] for s in students]

        average = sum(marks) / len(marks)

        highest = max(marks)

        lowest = min(marks)

        col1, col2, col3 = st.columns(
            3,
            gap="small"
        )

        with col1:

            render_html(f"""
            <div class="metric-card">

                <div class="metric-icon">📊</div>

                <div class="metric-label">
                    Class Average
                </div>

                <div class="metric-value">
                    {average:.1f}
                </div>

            </div>
            """)

        with col2:

            render_html(f"""
            <div class="metric-card">

                <div class="metric-icon">🏆</div>

                <div class="metric-label">
                    Highest Mark
                </div>

                <div class="metric-value">
                    {highest}
                </div>

            </div>
            """)

        with col3:

            render_html(f"""
            <div class="metric-card">

                <div class="metric-icon">📉</div>

                <div class="metric-label">
                    Lowest Mark
                </div>

                <div class="metric-value">
                    {lowest}
                </div>

            </div>
            """)

        render_html(f"""
        <br>

        <span class="student-count">
            👥 {len(students)} Students Added
        </span>
        """)

    else:

        render_html("""
        <div class="metric-card">

            <div class="metric-icon">📚</div>

            <div class="metric-label">
                Class Overview
            </div>

            <div class="metric-value">
                --
            </div>

            <p style="color:#94A0B2;font-size:12px;">
                Add students to view class statistics.
            </p>

        </div>
        """)


# ==========================================
# 10. STUDENT RESULTS
# ==========================================

st.markdown("<br>", unsafe_allow_html=True)

render_html("""
<div class="section-title">
    Student Results
</div>

<div class="section-subtitle">
    View all student marks and their grades.
</div>
""")

students = st.session_state.students

if students:

    table_rows = ""

    for index, student in enumerate(students, start=1):

        safe_name = html.escape(student["Name"])

        mark_value = student["Mark"]

        grade = student["Grade"].lower()

        table_rows += f"""
        <tr>

            <td>{index:02d}</td>

            <td>
                <strong>{safe_name}</strong>
            </td>

            <td>{mark_value}</td>

            <td>
                <span class="grade grade-{grade}">
                    {grade.upper()}
                </span>
            </td>

        </tr>
        """

    render_html(f"""
    <div class="table-wrap">

        <table class="student-table">

            <thead>

                <tr>
                    <th>#</th>
                    <th>Student Name</th>
                    <th>Marks</th>
                    <th>Grade</th>
                </tr>

            </thead>

            <tbody>

                {table_rows}

            </tbody>

        </table>

    </div>
    """)

else:

    render_html("""
    <div class="empty-state">

        <div class="empty-icon">
            📋
        </div>

        <div class="empty-title">
            No Students Added Yet
        </div>

        <p style="font-size:13px;">
            Start by adding your first student
            using the form above.
        </p>

    </div>
    """)


# ==========================================
# 11. FOOTER
# ==========================================

render_html("""
<div class="footer">
    Student Grade Manager |
    Built with Python and Streamlit
</div>
""")
