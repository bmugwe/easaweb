from django import forms


# usable list
KIND_OF_PACKAGE = (
    ("0", "Select Package Kind"),
    ("1", "Cardboard/Fiberboard"),
    ("2", "Bagged Cargo"),
    ("3", "Wooden Cases"),
    ("4", "Wooden Crates"),
    ("5", "Steel Drums"),
    ("6", "Bales"),
    ("7", "Palletizing Cargo"),
    ("8", "Containers"),
)


COUNTRIES = (
    ("0", "Select Country"),
    ("1", "Burundi"),
    ("2", "Democratic Republic of Congo"),
    ("3", "Kenya"),
    ("4", "Rwanda"),
    ("5", "South Sudan"),
    ("6", "Tanzania"),
    ("7", "Uganda"),
)

CHARGEs_TYPE = (("0", "Prepaid"), ("1", "Collect"))

AWB_CHARGES = (
    ("0", "CHGS code  (Charge Code ):"),
    ("PP", "All Charges Prepaid Cash"),
    ("PX", "All Charges Prepaid Credit"),
    ("PZ", "All Charges Prepaid by Credit Card"),
    ("PG", "All Charges Prepaid by GBL"),
    ("CP", "Destination Collect Cash"),
    ("CX", "Destination Collect Credit"),
    ("CM", "Destination Collect by MCO"),
    ("NC", "No Charge"),
    ("NT", "No Weight Charge - Other Charges Collect"),
    ("NZ", "No Weight Charge - Other Charges Prepaid by Credit Card"),
    ("NG", "No Weight Charge - Other Charges Prepaid by GBL"),
    ("NP", "No Weight Charge - Other Charges Prepaid Cash"),
    ("NX", "No Weight Charge - Other Charges Prepaid Credit"),
    ("CA", "Partial Collect Credit - Partial Prepaid Cash"),
    ("CB", "Partial Collect Credit - Partial Prepaid Credit"),
    ("CE", "Partial Collect Credit Card - Partial Prepaid Cash"),
    ("CH", "Partial Collect Credit Card - Partial Prepaid Credit"),
    ("PC", "Partial Prepaid Cash - Partial Collect Cash"),
    ("PD", "Partial Prepaid Credit - Partial Collect Cash"),
    ("PE", "Partial Prepaid Credit Card - Partial Collect Cash"),
    ("PH", "Partial Prepaid Credit Card - Partial Collect Credit"),
    ("PF", "Partial Prepaid Credit Card - Partial Collect Credit Card"),
)


class Invoicetemplate(forms.Form):
    from_companyname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": ("From Company.."),
                "class": "form-control",
                "id": "from_companyname",
            }
        )
    )

    from_personname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": ("From Person Name"),
                "class": "form-control",
                "id": "from_personname",
            }
        )
    )
    from_address = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": ("From Address"),
                "class": "form-control",
                "id": "from_address",
            }
        )
    )

    from_phonenumber = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": ("From Phone No."),
                "class": "form-control",
                "id": "from_phonenumber",
            }
        )
    )
    from_town = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": ("From Town"),
                "class": "form-control",
                "id": "from_town",
            }
        )
    )

    from_emailaddress = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": ("From Email"),
                "class": "form-control",
                "id": "from_emailaddress",
            }
        )
    )
    to_consigneeename = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": ("To Person"),
                "class": "form-control",
                "id": "to_consigneeename",
            }
        )
    )

    to_phonenumber = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": ("Phone No.:"),
                "class": "form-control",
                "id": "to_phonenumber",
            }
        )
    )
    to_address = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": ("To address"),
                "class": "form-control",
                "id": "to_address",
            }
        )
    )

    to_town = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": ("Destination Town"),
                "class": "form-control",
                "id": "to_town",
            }
        )
    )

    disbursement_date = forms.DateField(
        widget=forms.TextInput(
            attrs={
                "placeholder": ("Disbursement Date"),
                "class": "form-control",
                "id": "disbursement_date",
                "data-parsley-required": "true",
                "data-parsley-group": "group0"
                # type': 'hidden'
            }
        )
    )

    from_countries = forms.ChoiceField(
        choices=COUNTRIES,
        initial="0",
        widget=forms.Select(
            attrs={
                "class": "form-control",
                "id": "fromcountry",
                "data-parsley-required": "true",
                "data-parsley-group": "group0",
            }
        ),
    )

    from_town = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": ("From Town"),
                "class": "form-control",
                "id": "from_companyname",
            }
        )
    )

    to_countries = forms.ChoiceField(
        choices=COUNTRIES,
        initial="0",
        widget=forms.Select(
            attrs={
                "class": "form-control",
                "id": "fromcountry",
                "data-parsley-required": "true",
                "data-parsley-group": "group0",
            }
        ),
    )

    to_town = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": ("To town"),
                "class": "form-control",
                "id": "from_companyname",
            }
        )
    )

    package_kind = forms.ChoiceField(
        choices=KIND_OF_PACKAGE,
        initial="0",
        widget=forms.Select(
            attrs={
                "class": "form-control",
                "id": "fromcountry",
                "data-parsley-required": "true",
                "data-parsley-group": "group0",
            }
        ),
    )

    quantity = forms.IntegerField(min_value=0, required=True)

    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": ("Description of goods"),
                "class": "form-control",
                "rows": "3",
                "id": "Description",
                "data-parsley-required": "true",
                "data-parsley-group": "group2",
            }
        ),
    )

    weight = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": ("Weight (Kgs)"),
                "class": "form-control",
                "id": "weight",
            }
        )
    )

    length = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": ("Length (M)"),
                "class": "form-control",
                "id": "length",
            }
        )
    )

    width = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": ("Width (M)"),
                "class": "form-control",
                "id": "width",
            }
        )
    )

    height = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": ("Height (M)"),
                "class": "form-control",
                "id": "height",
            }
        )
    )

    airfreight_charges = forms.ChoiceField(
        choices=CHARGEs_TYPE,
        widget=forms.RadioSelect(
            # renderer=RadioCustomRenderer,
            attrs={
                "data-parsley-required": "true",
                "id": "airfreight_charges"
                # 'data-parsley-errors-container': "#errorfield"
            }
        ),
    )

    other_charges = forms.ChoiceField(
        choices=CHARGEs_TYPE,
        widget=forms.RadioSelect(
            # renderer=RadioCustomRenderer,
            attrs={
                "data-parsley-required": "true",
                "id": "other_charges"
                # 'data-parsley-errors-container': "#errorfield"
            }
        ),
    )

    insur_amount = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": ("Amount (KES)"),
                "class": "form-control",
                "id": "insurance_amount",
            }
        )
    )

    nvd = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": ("NVD"),
                "class": "form-control",
                "id": "nncdd",
            }
        )
    )

    ncv = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": ("NCV"),
                "class": "form-control",
                "id": "ncv",
            }
        )
    )

    accept = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            # renderer=RadioCustomRenderer,
            attrs={"data-parsley-required": "false"}
        ),
    )

    handling_info = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": ("Handling Infor and remarks"),
                "class": "form-control",
                "rows": "3",
                "id": "HANDLING_INFO",
                "data-parsley-required": "true",
                "data-parsley-group": "group2",
            }
        ),
    )


class Airwaybill(forms.Form):
    from_companyname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": ("From Company.."),
                "class": "form-control",
                "id": "from_companyname",
            }
        )
    )

    from_personname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": ("From Person Name"),
                "class": "form-control",
                "id": "from_personname",
            }
        )
    )
    from_address = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": ("From Address"),
                "class": "form-control",
                "id": "from_address",
            }
        )
    )

    from_phonenumber = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": ("From Phone No."),
                "class": "form-control",
                "id": "from_phonenumber",
            }
        )
    )
    from_town = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": ("From Town"),
                "class": "form-control",
                "id": "from_town",
            }
        )
    )

    from_emailaddress = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": ("From Email"),
                "class": "form-control",
                "id": "from_emailaddress",
            }
        )
    )
    to_consigneeename = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": ("To Person"),
                "class": "form-control",
                "id": "to_consigneeename",
            }
        )
    )

    to_phonenumber = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": ("Phone No.:"),
                "class": "form-control",
                "id": "to_phonenumber",
            }
        )
    )
    to_address = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": ("To address"),
                "class": "form-control",
                "id": "to_address",
            }
        )
    )

    to_town = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": ("Destination Town"),
                "class": "form-control",
                "id": "to_town",
            }
        )
    )

    disbursement_date = forms.DateField(
        widget=forms.TextInput(
            attrs={
                "placeholder": ("Disbursement Date"),
                "class": "form-control",
                "id": "disbursement_date",
                "data-parsley-required": "true",
                "data-parsley-group": "group0"
                # type': 'hidden'
            }
        )
    )

    from_countries = forms.ChoiceField(
        choices=COUNTRIES,
        initial="0",
        widget=forms.Select(
            attrs={
                "class": "form-control",
                "id": "fromcountry",
                "data-parsley-required": "true",
                "data-parsley-group": "group0",
            }
        ),
    )

    from_town = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": ("From Town"),
                "class": "form-control",
                "id": "from_companyname",
            }
        )
    )

    to_countries = forms.ChoiceField(
        choices=COUNTRIES,
        initial="0",
        widget=forms.Select(
            attrs={
                "class": "form-control",
                "id": "fromcountry",
                "data-parsley-required": "true",
                "data-parsley-group": "group0",
            }
        ),
    )

    to_town = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": ("To town"),
                "class": "form-control",
                "id": "from_companyname",
            }
        )
    )

    package_kind = forms.ChoiceField(
        choices=KIND_OF_PACKAGE,
        initial="0",
        widget=forms.Select(
            attrs={
                "class": "form-control",
                "id": "fromcountry",
                "data-parsley-required": "true",
                "data-parsley-group": "group0",
            }
        ),
    )

    quantity = forms.IntegerField(min_value=0, required=True)

    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": ("Description of goods"),
                "class": "form-control",
                "rows": "3",
                "id": "Description",
                "data-parsley-required": "true",
                "data-parsley-group": "group2",
            }
        ),
    )

    weight = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": ("Weight (Kgs)"),
                "class": "form-control",
                "id": "weight",
            }
        )
    )

    length = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": ("Length (M)"),
                "class": "form-control",
                "id": "length",
            }
        )
    )

    width = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": ("Width (M)"),
                "class": "form-control",
                "id": "width",
            }
        )
    )

    height = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": ("Height (M)"),
                "class": "form-control",
                "id": "height",
            }
        )
    )

    airfreight_charges = forms.ChoiceField(
        choices=CHARGEs_TYPE,
        widget=forms.RadioSelect(
            # renderer=RadioCustomRenderer,
            attrs={
                "data-parsley-required": "true",
                "id": "airfreight_charges"
                # 'data-parsley-errors-container': "#errorfield"
            }
        ),
    )

    other_charges = forms.ChoiceField(
        choices=CHARGEs_TYPE,
        widget=forms.RadioSelect(
            # renderer=RadioCustomRenderer,
            attrs={
                "data-parsley-required": "true",
                "id": "other_charges"
                # 'data-parsley-errors-container': "#errorfield"
            }
        ),
    )

    insur_amount = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": ("Amount (KES)"),
                "class": "form-control",
                "id": "insurance_amount",
            }
        )
    )

    nvd = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": ("NVD"),
                "class": "form-control",
                "id": "nncdd",
            }
        )
    )

    ncv = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": ("NCV"),
                "class": "form-control",
                "id": "ncv",
            }
        )
    )

    accept = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            # renderer=RadioCustomRenderer,
            attrs={"data-parsley-required": "false"}
        ),
    )

    handling_info = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": ("Handling Infor and remarks"),
                "class": "form-control",
                "rows": "3",
                "id": "HANDLING_INFO",
                "data-parsley-required": "true",
                "data-parsley-group": "group2",
            }
        ),
    )
