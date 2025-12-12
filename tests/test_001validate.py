import pytest
from pathlib import Path
from bento_mdf.validator import MDFValidator
from bento_transforms.mdf import TransformReader
from pdb import set_trace

tdir = Path("tests/").resolve() if Path("tests").exists() else Path().resolve()
test_transform_file = tdir / "samples" / "transforms.yaml"
test_mdfschema_file = tdir / "samples" / "mdf-schema-tf.yaml"

def test_file(s):
    return tdir / "samples" / s

def test_reader():
    val = MDFValidator(test_mdfschema_file, test_transform_file, raise_error=True)
    assert val.load_and_validate_schema()
    assert val.load_and_validate_yaml()
    assert val.validate_instance_with_schema()
    tmdf = TransformReader(test_transform_file,
                           handle='transforms',
                           mdf_schema=test_mdfschema_file)
    assert tmdf
    assert tmdf.mdf['TransformDefinitions']
    assert tmdf.mdf_schema['$id']

def test_err_missing_default_in_From():
    with pytest.raises(RuntimeError, match="Version not specified"):
        TransformReader(test_file("err_1.yaml"),
                           handle='transforms',
                           mdf_schema=test_mdfschema_file)

def test_err_missing_default_in_To():
    with pytest.raises(RuntimeError, match="Version not specified"):
        TransformReader(test_file("err_2.yaml"),
                           handle='transforms',
                           mdf_schema=test_mdfschema_file)

def test_node_default_works_in_from():
    assert TransformReader(test_file("good_3.yaml"),
                           handle='transforms',
                           mdf_schema=test_mdfschema_file)

def test_err_missing_node_default_in_to():
    with pytest.raises(RuntimeError, match="Node not specified"):
        TransformReader(test_file("err_4.yaml"),
                           handle='transforms',
                           mdf_schema=test_mdfschema_file)

def test_err_missing_package_default_in_step():
    with pytest.raises(RuntimeError, match="Simple step entrypoint format"):
        TransformReader(test_file("err_5.yaml"),
                           handle='transforms',
                           mdf_schema=test_mdfschema_file)

