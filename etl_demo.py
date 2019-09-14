from feature_lib.etl_abc import AbstractEtl


class Etl(AbstractEtl):
    def extract(self):
        self.df.dropna(subset=["user_id"], inplace=True)
        self.df["creation_to_binding"] = self.df.binding_date - self.df.creation_date
        return self.df
