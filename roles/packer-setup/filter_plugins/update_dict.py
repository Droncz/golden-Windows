class FilterModule(object):
    def filters(self):
        return {
            'update_dict': self.update_dict,
            'merge_dict': self.merge_dict,
            'del_key': self.del_key,
        }

    def update_dict(self, old_dict, key, value):
        old_dict[key] = value
        return old_dict

    def merge_dict(self, old_dict, new_dict):
        old_dict.update(new_dict)
        return old_dict

    def del_key(self, old_dict, key):
        del old_dict[key]
        return old_dict
