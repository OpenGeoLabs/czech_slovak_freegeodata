<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis maxScale="0" simplifyLocal="1" simplifyDrawingTol="1" styleCategories="AllStyleCategories" minScale="100000000" labelsEnabled="0" version="3.14.16-Pi" hasScaleBasedVisibilityFlag="0" simplifyAlgorithm="0" simplifyDrawingHints="1" simplifyMaxScale="1" readOnly="0">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <temporal durationField="" accumulate="0" startField="" durationUnit="min" enabled="0" endExpression="" mode="0" endField="" fixedDuration="0" startExpression="">
    <fixedRange>
      <start></start>
      <end></end>
    </fixedRange>
  </temporal>
  <renderer-v2 type="singleSymbol" enableorderby="0" symbollevels="0" forceraster="0">
    <symbols>
      <symbol type="line" clip_to_extent="1" force_rhr="0" name="0" alpha="1">
        <layer pass="0" class="SimpleLine" enabled="1" locked="0">
          <prop k="capstyle" v="round"/>
          <prop k="customdash" v="0.66;2"/>
          <prop k="customdash_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="customdash_unit" v="MM"/>
          <prop k="draw_inside_polygon" v="0"/>
          <prop k="joinstyle" v="round"/>
          <prop k="line_color" v="182,72,94,255"/>
          <prop k="line_style" v="solid"/>
          <prop k="line_width" v="0.6"/>
          <prop k="line_width_unit" v="MM"/>
          <prop k="offset" v="0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="ring_filter" v="0"/>
          <prop k="use_custom_dash" v="1"/>
          <prop k="width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </symbols>
    <rotation/>
    <sizescale/>
  </renderer-v2>
  <customproperties>
    <property key="embeddedWidgets/count" value="0"/>
    <property key="variableNames"/>
    <property key="variableValues"/>
  </customproperties>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <SingleCategoryDiagramRenderer diagramType="Histogram" attributeLegend="1">
    <DiagramCategory minimumSize="0" opacity="1" sizeScale="3x:0,0,0,0,0,0" scaleBasedVisibility="0" enabled="0" spacingUnitScale="3x:0,0,0,0,0,0" spacing="5" backgroundColor="#ffffff" barWidth="5" sizeType="MM" diagramOrientation="Up" showAxis="1" width="15" penAlpha="255" direction="0" penColor="#000000" labelPlacementMethod="XHeight" maxScaleDenominator="1e+08" penWidth="0" spacingUnit="MM" backgroundAlpha="255" minScaleDenominator="0" lineSizeScale="3x:0,0,0,0,0,0" rotationOffset="270" lineSizeType="MM" height="15" scaleDependency="Area">
      <fontProperties style="" description="MS Shell Dlg 2,8.25,-1,5,50,0,0,0,0,0"/>
      <axisSymbol>
        <symbol type="line" clip_to_extent="1" force_rhr="0" name="" alpha="1">
          <layer pass="0" class="SimpleLine" enabled="1" locked="0">
            <prop k="capstyle" v="square"/>
            <prop k="customdash" v="5;2"/>
            <prop k="customdash_map_unit_scale" v="3x:0,0,0,0,0,0"/>
            <prop k="customdash_unit" v="MM"/>
            <prop k="draw_inside_polygon" v="0"/>
            <prop k="joinstyle" v="bevel"/>
            <prop k="line_color" v="35,35,35,255"/>
            <prop k="line_style" v="solid"/>
            <prop k="line_width" v="0.26"/>
            <prop k="line_width_unit" v="MM"/>
            <prop k="offset" v="0"/>
            <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
            <prop k="offset_unit" v="MM"/>
            <prop k="ring_filter" v="0"/>
            <prop k="use_custom_dash" v="0"/>
            <prop k="width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
            <data_defined_properties>
              <Option type="Map">
                <Option type="QString" name="name" value=""/>
                <Option name="properties"/>
                <Option type="QString" name="type" value="collection"/>
              </Option>
            </data_defined_properties>
          </layer>
        </symbol>
      </axisSymbol>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings priority="0" showAll="1" obstacle="0" dist="0" linePlacementFlags="18" placement="2" zIndex="0">
    <properties>
      <Option type="Map">
        <Option type="QString" name="name" value=""/>
        <Option name="properties"/>
        <Option type="QString" name="type" value="collection"/>
      </Option>
    </properties>
  </DiagramLayerSettings>
  <geometryOptions removeDuplicateNodes="0" geometryPrecision="0">
    <activeChecks/>
    <checkConfiguration/>
  </geometryOptions>
  <referencedLayers/>
  <referencingLayers/>
  <fieldConfiguration>
    <field name="KOD">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="SHAPE_Leng">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="DATA50_K">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="DATA50_P">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
  </fieldConfiguration>
  <aliases>
    <alias field="KOD" name="" index="0"/>
    <alias field="SHAPE_Leng" name="" index="1"/>
    <alias field="DATA50_K" name="" index="2"/>
    <alias field="DATA50_P" name="" index="3"/>
  </aliases>
  <excludeAttributesWMS/>
  <excludeAttributesWFS/>
  <defaults>
    <default field="KOD" expression="" applyOnUpdate="0"/>
    <default field="SHAPE_Leng" expression="" applyOnUpdate="0"/>
    <default field="DATA50_K" expression="" applyOnUpdate="0"/>
    <default field="DATA50_P" expression="" applyOnUpdate="0"/>
  </defaults>
  <constraints>
    <constraint field="KOD" constraints="0" unique_strength="0" exp_strength="0" notnull_strength="0"/>
    <constraint field="SHAPE_Leng" constraints="0" unique_strength="0" exp_strength="0" notnull_strength="0"/>
    <constraint field="DATA50_K" constraints="0" unique_strength="0" exp_strength="0" notnull_strength="0"/>
    <constraint field="DATA50_P" constraints="0" unique_strength="0" exp_strength="0" notnull_strength="0"/>
  </constraints>
  <constraintExpressions>
    <constraint field="KOD" exp="" desc=""/>
    <constraint field="SHAPE_Leng" exp="" desc=""/>
    <constraint field="DATA50_K" exp="" desc=""/>
    <constraint field="DATA50_P" exp="" desc=""/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction key="Canvas" value="{00000000-0000-0000-0000-000000000000}"/>
  </attributeactions>
  <attributetableconfig sortExpression="" sortOrder="0" actionWidgetStyle="dropDown">
    <columns>
      <column type="field" name="KOD" width="-1" hidden="0"/>
      <column type="field" name="SHAPE_Leng" width="-1" hidden="0"/>
      <column type="field" name="DATA50_K" width="-1" hidden="0"/>
      <column type="field" name="DATA50_P" width="-1" hidden="0"/>
      <column type="actions" width="-1" hidden="1"/>
    </columns>
  </attributetableconfig>
  <conditionalstyles>
    <rowstyles/>
    <fieldstyles/>
  </conditionalstyles>
  <storedexpressions/>
  <editform tolerant="1"></editform>
  <editforminit/>
  <editforminitcodesource>0</editforminitcodesource>
  <editforminitfilepath></editforminitfilepath>
  <editforminitcode><![CDATA[# -*- coding: utf-8 -*-
"""
QGIS forms can have a Python function that is called when the form is
opened.

Use this function to add extra logic to your forms.

Enter the name of the function in the "Python Init function"
field.
An example follows:
"""
from qgis.PyQt.QtWidgets import QWidget

def my_form_open(dialog, layer, feature):
	geom = feature.geometry()
	control = dialog.findChild(QWidget, "MyLineEdit")
]]></editforminitcode>
  <featformsuppress>0</featformsuppress>
  <editorlayout>generatedlayout</editorlayout>
  <editable>
    <field editable="1" name="DATA50_K"/>
    <field editable="1" name="DATA50_P"/>
    <field editable="1" name="KOD"/>
    <field editable="1" name="SHAPE_Leng"/>
  </editable>
  <labelOnTop>
    <field name="DATA50_K" labelOnTop="0"/>
    <field name="DATA50_P" labelOnTop="0"/>
    <field name="KOD" labelOnTop="0"/>
    <field name="SHAPE_Leng" labelOnTop="0"/>
  </labelOnTop>
  <dataDefinedFieldProperties/>
  <widgets/>
  <previewExpression>"KOD"</previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>1</layerGeometryType>
</qgis>
