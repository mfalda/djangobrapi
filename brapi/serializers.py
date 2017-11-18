from rest_framework import serializers

 
class ExtendedSerializer(serializers.ModelSerializer):

    def get_field_names(self, declared_fields, info):
        
        expanded_fields = super(ExtendedSerializer, self).get_field_names(declared_fields, info)

        if getattr(self.Meta, 'excluded', None):
            expanded_fields = set(expanded_fields) - set(self.Meta.excluded)
        # end if
        
        if getattr(self.Meta, 'extra_fields', None):
            return list(expanded_fields) + self.Meta.extra_fields
        else:
            return list(expanded_fields)
        # end if
        
    # end def get_field_names
        
# end class ExtendedSerializer
            