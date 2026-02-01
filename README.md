## Hugging Face Model

**https://huggingface.co/DATEXIS/CORe-clinical-diagnosis-prediction**

## Cases of use

**The information is organized by the next schema**

> MAIN SYMPTOM

> SYMPTOM DETAILS

> OTHER SYMPTOMS

> DURATION

> PAST HISTORY / RISK FACTORS

> MEDS & ALLERGIES (patient-reported)

**Case 1**
```bash
MAIN SYMPTOM: Chest pain.

SYMPTOM DETAILS (OPQRST):
- Onset: Started about 2 hours ago.
- Provocation/Palliation: Began at rest; not clearly relieved by changing position. Took aspirin with little improvement.
- Quality: Pressure/tightness.
- Region/Radiation: Center of chest, radiates to left arm and jaw.
- Severity: 8/10.
- Time course: Constant since onset.

OTHER SYMPTOMS:
- Sweating/diaphoresis, nausea.
- No fever. No cough.

DURATION: 2 hours.

PAST HISTORY / RISK FACTORS:
- Known high blood pressure and high cholesterol.
- Former smoker.

MEDS & ALLERGIES (patient-reported):
- Meds: Blood pressure medication and a cholesterol medication (names not known).
- Allergies: None known.
```
> API
```JSON
{
  "text": "MAIN SYMPTOM: Chest pain.\n\nSYMPTOM DETAILS (OPQRST):\n- Onset: Started about 2 hours ago.\n- Provocation/Palliation: Began at rest; not clearly relieved by changing position. Took aspirin with little improvement.\n- Quality: Pressure/tightness.\n- Region/Radiation: Center of chest, radiates to left arm and jaw.\n- Severity: 8/10.\n- Time course: Constant since onset.\n\nOTHER SYMPTOMS:\n- Sweating/diaphoresis, nausea.\n- No fever. No cough.\n\nDURATION: 2 hours.\n\nPAST HISTORY / RISK FACTORS:\n- Known high blood pressure and high cholesterol.\n- Former smoker.\n\nMEDS & ALLERGIES (patient-reported):\n- Meds: Blood pressure medication and a cholesterol medication (names not known).\n- Allergies: None known.",
  "top_n": 5,
  "threshold": 0.3,
  "include_children": true,
  "max_children": 5
}
```

**Case 2**
```bash
MAIN SYMPTOM: Fever and shortness of breath.

SYMPTOM DETAILS (OPQRST):
- Onset: Started 3 days ago.
- Provocation/Palliation: Worse with walking and lying flat; better sitting up.
- Quality: Trouble breathing and chest discomfort when taking deep breaths.
- Region/Radiation: Chest discomfort, no radiation.
- Severity: Breathing difficulty 7/10.
- Time course: Gradually worsening.

OTHER SYMPTOMS:
- Productive cough with yellow sputum, chills, fatigue.
- Feels more confused today.
- No burning with urination.

DURATION: 3 days.

PAST HISTORY / RISK FACTORS:
- COPD and type 2 diabetes.

MEDS & ALLERGIES (patient-reported):
- Meds: Inhalers; diabetes pill (metformin).
- Allergies: Penicillin (rash).
```
> API
```JSON
{
  "text": "MAIN SYMPTOM: Fever and shortness of breath.\n\nSYMPTOM DETAILS (OPQRST):\n- Onset: Started 3 days ago.\n- Provocation/Palliation: Worse with walking and lying flat; better sitting up.\n- Quality: Trouble breathing and chest discomfort when taking deep breaths.\n- Region/Radiation: Chest discomfort, no radiation.\n- Severity: Breathing difficulty 7/10.\n- Time course: Gradually worsening.\n\nOTHER SYMPTOMS:\n- Productive cough with yellow sputum, chills, fatigue.\n- Feels more confused today.\n- No burning with urination.\n\nDURATION: 3 days.\n\nPAST HISTORY / RISK FACTORS:\n- COPD and type 2 diabetes.\n\nMEDS & ALLERGIES (patient-reported):\n- Meds: Inhalers; diabetes pill (metformin).\n- Allergies: Penicillin (rash).",
  "top_n": 5,
  "threshold": 0.3,
  "include_children": true,
  "max_children": 5
}
```


**Case 3**
```bash
MAIN SYMPTOM: Vomiting and weakness.

SYMPTOM DETAILS (OPQRST):
- Onset: Started yesterday.
- Provocation/Palliation: Worse when trying to eat or drink; nothing helps much.
- Quality: Nausea, repeated vomiting, stomach pain.
- Region/Radiation: Abdominal discomfort, no radiation.
- Severity: 7/10.
- Time course: Worsening.

OTHER SYMPTOMS:
- Very thirsty, frequent urination.
- Feeling very tired.
- No fever. No cough.

DURATION: 1 day.

PAST HISTORY / RISK FACTORS:
- Type 1 diabetes.

MEDS & ALLERGIES (patient-reported):
- Meds: Insulin, but missed doses for 2 days.
- Allergies: None known.
```
> API
```JSON
{
  "text": "MAIN SYMPTOM: Vomiting and weakness.\n\nSYMPTOM DETAILS (OPQRST):\n- Onset: Started yesterday.\n- Provocation/Palliation: Worse when trying to eat or drink; nothing helps much.\n- Quality: Nausea, repeated vomiting, stomach pain.\n- Region/Radiation: Abdominal discomfort, no radiation.\n- Severity: 7/10.\n- Time course: Worsening.\n\nOTHER SYMPTOMS:\n- Very thirsty, frequent urination.\n- Feeling very tired.\n- No fever. No cough.\n\nDURATION: 1 day.\n\nPAST HISTORY / RISK FACTORS:\n- Type 1 diabetes.\n\nMEDS & ALLERGIES (patient-reported):\n- Meds: Insulin, but missed doses for 2 days.\n- Allergies: None known.",
  "top_n": 5,
  "threshold": 0.3,
  "include_children": true,
  "max_children": 5
}
```

**Case 4**
```bash
MAIN SYMPTOM: Sudden weakness and trouble speaking.

SYMPTOM DETAILS (OPQRST):
- Onset: Started suddenly about 1 hour ago.
- Provocation/Palliation: No clear trigger; nothing improves it.
- Quality: Weakness and difficulty speaking.
- Region/Radiation: Weakness on the right side of the body; face feels droopy on one side.
- Severity: Severe (unable to use right arm normally).
- Time course: Constant since it started.

OTHER SYMPTOMS:
- No headache.
- No recent trauma.

DURATION: 1 hour.

PAST HISTORY / RISK FACTORS:
- Irregular heartbeat (atrial fibrillation) and high blood pressure.
- Not taking blood thinner medication currently.

MEDS & ALLERGIES (patient-reported):
- Meds: Heart rate medication; aspirin.
- Allergies: None known.
```
> API
```JSON
{
  "text": "MAIN SYMPTOM: Sudden weakness and trouble speaking.\n\nSYMPTOM DETAILS (OPQRST):\n- Onset: Started suddenly about 1 hour ago.\n- Provocation/Palliation: No clear trigger; nothing improves it.\n- Quality: Weakness and difficulty speaking.\n- Region/Radiation: Weakness on the right side of the body; face feels droopy on one side.\n- Severity: Severe (unable to use right arm normally).\n- Time course: Constant since it started.\n\nOTHER SYMPTOMS:\n- No headache.\n- No recent trauma.\n\nDURATION: 1 hour.\n\nPAST HISTORY / RISK FACTORS:\n- Irregular heartbeat (atrial fibrillation) and high blood pressure.\n- Not taking blood thinner medication currently.\n\nMEDS & ALLERGIES (patient-reported):\n- Meds: Heart rate medication; aspirin.\n- Allergies: None known.",
  "top_n": 5,
  "threshold": 0.3,
  "include_children": true,
  "max_children": 5
}
```

**Case 5**
```bash
MAIN SYMPTOM: Shortness of breath and leg swelling.

SYMPTOM DETAILS (OPQRST):
- Onset: Worsening over the past week.
- Provocation/Palliation: Worse with walking and when lying down; better sitting up.
- Quality: Feeling out of breath; needs extra pillows to sleep.
- Region/Radiation: Breathing issue, no radiation.
- Severity: 6/10.
- Time course: Gradually worsening.

OTHER SYMPTOMS:
- Weight gain and swelling in both legs.
- Less urination than usual.
- No fever. No productive cough.

DURATION: 1 week.

PAST HISTORY / RISK FACTORS:
- Heart failure and coronary artery disease.
- High blood pressure.

MEDS & ALLERGIES (patient-reported):
- Meds: “Water pill” (diuretic) but missed several doses; blood pressure meds.
- Allergies: None known.
```
> API
```JSON
{
  "text": "MAIN SYMPTOM: Shortness of breath and leg swelling.\n\nSYMPTOM DETAILS (OPQRST):\n- Onset: Worsening over the past week.\n- Provocation/Palliation: Worse with walking and when lying down; better sitting up.\n- Quality: Feeling out of breath; needs extra pillows to sleep.\n- Region/Radiation: Breathing issue, no radiation.\n- Severity: 6/10.\n- Time course: Gradually worsening.\n\nOTHER SYMPTOMS:\n- Weight gain and swelling in both legs.\n- Less urination than usual.\n- No fever. No productive cough.\n\nDURATION: 1 week.\n\nPAST HISTORY / RISK FACTORS:\n- Heart failure and coronary artery disease.\n- High blood pressure.\n\nMEDS & ALLERGIES (patient-reported):\n- Meds: “Water pill” (diuretic) but missed several doses; blood pressure meds.\n- Allergies: None known.",
  "top_n": 5,
  "threshold": 0.3,
  "include_children": true,
  "max_children": 5
}
```

