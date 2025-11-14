# models.py

from django.db import models

from student.models import Student
from subjects.models import TbTypeEvaluation, Subject


# The main model for the "note" table
class Note(models.Model):
    # Primary key: Auto-incrementing ID
    id_note = models.AutoField(primary_key=True, db_column='id_note')

    # Foreign key to Student (references student.st_id)
    # In Django, ForeignKey automatically links to the primary key of the related model.
    # The field name is kept as 'st_id' to match the original table, but it's a ForeignKey object.
    st_id = models.ForeignKey(
        Student,
        # Adjust on_delete as per your business logic (e.g., CASCADE, SET_NULL)
        on_delete=models.CASCADE,
        db_column='st_id'  # Ensures the database column name matches
    )

    # Foreign key to Subject (references tb_subject.id_sub)
    id_sub = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        db_column='id_sub'
    )

    # Foreign key to TbTypeEvaluation (references tb_type_evaluation.id_type_eval)
    id_type_eval = models.ForeignKey(
        TbTypeEvaluation,
        on_delete=models.CASCADE,
        db_column='id_type_eval'
    )

    # School year (NUMERIC in PostgreSQL, mapped to DecimalField for precision)
    # Assumed max_digits=10 and decimal_places=2; adjust if needed based on your data.
    scolar_year = models.PositiveIntegerField(
        db_column='scolar_year'
    )

    # Date and time of the note
    date_note = models.DateTimeField(db_column='date_note', db_index=True)

    # Value of the note (NUMERIC, mapped to DecimalField)
    value_note = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        db_column='value_note'
    )

    class Meta:
        db_table = 'note'  # Matches the original table name

    def __str__(self):
        return f"Note for {self.st_id} in {self.id_sub} ({self.id_type_eval}) - {self.value_note} (Year: {self.scolar_year})"
