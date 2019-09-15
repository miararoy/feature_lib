import pandas as pd

from abc import abstractmethod, ABC

class AbstractEtl(ABC):
    
    def __init__(self, df: pd.core.frame.DataFrame):
        self.df = df.copy()
        super(AbstractEtl, self).__init__()

    @abstractmethod
    def extract(self) -> pd.core.frame.DataFrame:
        """developer will have to implement this function for feature extraction
        for self.df
        
        Returns:
            df(pf.DataFrame): dataframe after doing feature extraction
        """
        pass
