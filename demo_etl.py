from feature_lib.etl_abc import AbstractEtl


class Etl(AbstractEtl):
    def extract(self):
        self.df.dropna(subset=["user_id"], inplace=True)
        self.df["creation_to_binding"] = self.df.binding_date - self.df.creation_date
        self.df.set_index("user_id", inplace=True)
        return self.df