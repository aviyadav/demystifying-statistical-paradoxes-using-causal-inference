import pandas as pd
import numpy as np
import statsmodels.api as sm
from .base import ParadoxExample

class SimpsonsParadox(ParadoxExample):
    """
    Simpson's Paradox occurs when a trend appears in several groups of data 
    but disappears or reverses when these groups are combined.
    """
    
    @property
    def name(self) -> str:
        return "Simpson's Paradox"

    @property
    def description(self) -> str:
        return (
            "Simpson's Paradox is a phenomenon in probability and statistics in which a trend appears "
            "in several groups of data but disappears or reverses when these groups are combined. "
            "This often happens when there is a lurking variable (confounder) that correlates with both "
            "the independent and dependent variables."
        )

    def _stats(self, g):
        applied = g['Freq'].sum()
        admitted = g.loc[g['Admit'] == 'Admitted', 'Freq'].sum()
        rate = admitted / applied if applied else 0
        return pd.Series({'Applied': applied, 'Admitted': admitted, 'Rate': rate})

    def _run_berkeley_admissions(self):
        print("\n--- Berkeley Admissions Dataset ---")
        df = sm.datasets.get_rdataset('UCBAdmissions', 'datasets').data
        
        # General admission by gender
        general_admission = df.groupby('Gender').apply(self._stats)
        general_admission['Applied'] = general_admission['Applied'].astype(int)
        general_admission['Admitted'] = general_admission['Admitted'].astype(int)
        general_admission['Rate'] = (general_admission['Rate'] * 100).round(1).astype(str) + '%'
        print("\nOverall Admission Rate by Gender:")
        print(general_admission.reset_index())

        # Admission by department and gender
        t = df.groupby(['Dept', 'Gender']).apply(self._stats).unstack('Gender')
        dept_admission = pd.DataFrame({
            'Dept':           t.index,
            'Men applied':    t[('Applied',  'Male')].astype(int).values,
            'Men admitted':   t[('Admitted', 'Male')].astype(int).values,
            'Men rate':       (t[('Rate', 'Male')]   * 100).round(1).astype(str).values + '%',
            'Women applied':  t[('Applied',  'Female')].astype(int).values,
            'Women admitted': t[('Admitted', 'Female')].astype(int).values,
            'Women rate':     (t[('Rate', 'Female')] * 100).round(1).astype(str).values + '%',
        })
        print("\nAdmission Rate by Department:")
        print(dept_admission)

    def _run_kidney_stones(self):
        print("\n--- Kidney Stone Treatment Dataset ---")
        kidney = pd.DataFrame({
            'Treatment':  ['A', 'A', 'B', 'B'],
            'Stone size': ['Small', 'Large', 'Small', 'Large'],
            'Successes':  [81, 192, 234, 55],
            'Total':      [87, 263, 270, 80]
        })

        kidney['Success rate (%)'] = (kidney['Successes'] / kidney['Total'] * 100).round(2).astype(str) + '%'
        print("\nSuccess Rate by Treatment and Stone Size:")
        print(kidney.set_index(['Treatment', 'Stone size']))

        overall = kidney.groupby('Treatment').agg(
            Successes = ('Successes', 'sum'),
            Total = ('Total', 'sum')
        )
        overall['Success rate (%)'] = (overall['Successes'] / overall['Total'] * 100).round(2).astype(str) + '%'
        print("\nOverall Success Rate by Treatment:")
        print(overall)

    def run(self) -> None:
        print(f"=== {self.name} ===")
        print(self.description)
        self._run_berkeley_admissions()
        self._run_kidney_stones()
