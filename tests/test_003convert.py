import pytest
from bento_transforms.mdf import TransformReader
from bento_transforms.converters.converter import create_transform_function
from typing import Callable
from pdb import set_trace

def test_tf_functions(samplesd):
    tmdf = TransformReader(samplesd / "tf_func_test.yaml",
                           handle='transforms',
                           mdf_schema=samplesd / "mdf-schema-tf.yaml")
    tf_func = create_transform_function(
        tmdf.transforms['fullname_to_fmlnames']
    )
    assert isinstance(tf_func, Callable)

    ret = tf_func("Sigismund Leonhart Popbutton")
    assert len(ret)==3

    ret = tf_func(study_personnel_personnel_name="Sigismund Leonhart Popbutton")
    assert ret['investigator_middle_name'] == "Leonhart"

    with pytest.raises(RuntimeError, match="Valid input keys are"):
        tf_func(**{"squidward": "Sigismund Leonhart Popbutton"})
