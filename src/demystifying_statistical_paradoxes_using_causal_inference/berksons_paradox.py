import pandas as pd
import numpy as np
from .base import ParadoxExample

class BerksonParadox(ParadoxExample):
    """
    Berkson's Paradox occurs when two independent variables appear to be negatively 
    correlated because the sample is restricted to a subset of the population 
    (selection bias).
    """
    
    @property
    def name(self) -> str:
        return "Berkson's Paradox"

    @property
    def description(self) -> str:
        return (
            "Berkson's Paradox is a type of selection bias that occurs when a sample is "
            "selected based on a criterion that is influenced by two independent variables. "
            "This creates a spurious negative correlation between those variables within "
            "the selected sample, even if they are independent in the general population."
        )

    def run(self) -> None:
        print(f"=== {self.name} ===")
        print(self.description)
        
        # Set up general population
        np.random.seed(42)
        n = 100000

        # Two independent attributes (e.g., intelligence and attractiveness)
        # We use binomials here to represent presence/absence of a trait
        attr1 = np.random.binomial(1, 0.20, n)
        attr2 = np.random.binomial(1, 0.20, n)

        # Selection criterion: "Success" if they have either attribute
        # In a real scenario, this could be "getting a job" or "getting into a university"
        # We simulate a selection process where having either trait increases the chance of selection
        p_select = 0.05 + 0.40 * attr1 + 0.40 * attr2
        selected = np.random.binomial(1, np.clip(p_select, 0, 1), n)

        df = pd.DataFrame({
            'Attribute_1': attr1,
            'Attribute_2': attr2,
            'Selected': selected
        })

        # In the general population: correlation between attributes
        corr_gen = df[['Attribute_1', 'Attribute_2']].corr().iloc[0, 1]
        print(f"\nGeneral population correlation: {corr_gen:.4f}")

        # Now condition on selection (the "Berkson" sample)
        selected_only = df[df['Selected'] == 1]
        corr_sel = selected_only[['Attribute_1', 'Attribute_2']].corr().iloc[0, 1]
        print(f"Correlation in selected sample: {corr_sel:.4f}")
        
        print("\nObservation: Even though the attributes were independent in the general population, "
              "they appear negatively correlated in the selected sample.")
