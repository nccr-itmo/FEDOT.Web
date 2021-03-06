def test_get_showcase_item_endpoint(client):
    case_id = 'item1'
    showcase_item_json = client.get(f'api/showcase/items/{case_id}').json

    assert showcase_item_json['case_id'] == case_id
    assert case_id in showcase_item_json['description']
    assert 'png' in showcase_item_json['icon_path']


def test_get_showcase_endpoint(client):
    showcase_json = client.get(f'api/showcase/').json

    assert 'item1' in showcase_json['items_uids']
    assert 'item3' in showcase_json['items_uids']
